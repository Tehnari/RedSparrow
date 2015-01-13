
import zmq
from zmq.eventloop import ioloop
ioloop.install()


import tornado
import tornado.web

import argparse
import logging
import os
import json
import sys, traceback


import tornado.web
from tornado.ioloop import IOLoop
from tornado_json.routes import get_routes
from tornado.log import enable_pretty_logging


from redsparrow.config import Config
import redsparrow.api as RedSparrowApi
from redsparrow.queue import  QueueReqMessage, ReplyQueue, QueueRepMessage
from redsparrow.orm import db
import redsparrow.methods as ZMQMethods
from redsparrow.methods.base import BaseMethod
from redsparrow.methods.methods_doc_gen import methods_doc_gen
from redsparrow.methods.router import get_methods as get_methods_zmq, Router
from redsparrow.plagiarism.periodic_detector import PeriodicDetector
enable_pretty_logging()

config = Config()
config.load('./config/config.yml')


class RedSparrow(tornado.web.Application):


    def __init__(self, routes, zmq_methods, settings, db_conn=None):
        # Generate API Documentation

        # Unless gzip was specifically set to False in settings, enable it
        if "gzip" not in list(settings.keys()):
            settings["gzip"] = True

        self.db_conn = db_conn
        self.queue = ReplyQueue(config['replyqueue'], self.on_data)
        self.periodic_detector = PeriodicDetector()
        BaseMethod.application = self
        self.router = Router(self)
        self.router.add_methods(zmq_methods)
        tornado.web.Application.__init__(
            self,
            routes,
            **settings
        )
    # @process
    def on_data(self, data):
        req = QueueReqMessage(json_data=data[0].decode("UTF-8"))
        try:
            self.router.find_method(req)
        except Exception as err:
            logging.error('Internal error {}, request {}'.format(err, req))
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback,
                                                  limit=2, file=sys.stderr)
            response = QueueRepMessage(id=req.id)
            response.error = {"code": -32603, "message": "Internal error %s" % err}
            self.send_response(response)

    def send_response(self, data):
        if data.error is not None:
            logging.error("Request with id {} failed with error {}".format(data.id, data.error))
        self.queue.send_json(str(data))
        self.queue.flush()





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="RedSparrow  - Command Line Interface")
    parser.add_argument("--port", action="store", help="listen port", default=8000)
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    logging.info('RedSparrow listen on %s' % args.port)

    routes = get_routes(RedSparrowApi)
    zmq_methods = get_methods_zmq(ZMQMethods)
    methods_doc_gen(zmq_methods)
    logging.info("ZMQ Methods\n======\n\n" + json.dumps(
        [(zmq_m['name'], repr(zmq_m['class'])) for zmq_m in zmq_methods],
        indent=2)
    )
    logging.info("Routes\n======\n\n" + json.dumps(
        [(url, repr(rh)) for url, rh in routes],
        indent=2)
    )

    db.bind('mysql', user=config['database']['user'], passwd=config['database']['password'],
        host=config['database']['host'], db=config['database']['database'])

    db.generate_mapping(check_tables=True, create_tables=True)
    application = RedSparrow(routes=routes, zmq_methods=zmq_methods, settings={}, db_conn=db)
    application.listen(args.port)

    IOLoop.instance().start()




