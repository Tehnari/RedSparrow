import multiprocessing as mp


from pony.orm import db_session, commit, flush

from redsparrow.orm import Thesis, Similarity, LinesWords
import redsparrow.plagiarism.levenshtein as Levenshtein
import redsparrow.plagiarism.rabinkarb as   RabinKarb
from redsparrow.extractor.winnowing import winnow
from redsparrow.keywords import calculate_keywords_similarity


class PlagiarismDetector(object):
    LINE_LENGHT = 80

    def __init__(self):
        self._toCheck = None

    def preprocess(self, thesis_id):
        pass
        # get data from db
        # get keyword
        # start processing in by neares keyword
    def winnowing(self, thesis1, thesis2, window=15):
        """ Function that return by characters similarity in text
            :param thesis1 - text
            :param thesis2  - text
            :returns list of touple (index1, index2)
        """

        winnows1 = winnow(thesis1, window)
        winnows2 = winnow(thesis2, window)
        reversed_dict2 = dict(zip(winnows2.values(), winnows2))
        result = []
        for index in winnows1.keys():
            if winnows1[index] in winnows2.values():
                second_index = reversed_dict2[winnows1[index]]
                result.append((index, second_index))
        return result

    def calculate_percentageSimilarity(self, winnowing_result, text_len):
        if len(winnowing_result) == 1:
            return 0
        winnowing_result = sorted(winnowing_result, key=lambda x: x[1], reverse=True)
        result = 0
        for i in range(0, len(winnowing_result) - 1, 1):
            result += winnowing_result[i][1] -  winnowing_result[i + 1][1]

        result = result /text_len
        return int(result * 100)
    def __calculate_keywords_similarity(self, kerwords1, kerwords2):
        list_key1 = [ key.keyword for key in kerwords1]
        list_key2 = [ key.keyword for key in kerwords2]
        return int(calculate_keywords_similarity(list_key1, list_key2) * 100)

    @db_session
    def process_one(self, thesis):
        winnowing_result = self.winnowing(self.__toCheck.text, thesis.text)
        lines = []
        percentageSimilarity = self.calculate_percentageSimilarity(winnowing_result, len(thesis.text))
        print(percentageSimilarity)
        similarity = Similarity(thesis1=self.__toCheck.id,
                                thesis2=thesis.id,
                                keywordSimilarity=self.__calculate_keywords_similarity(self.__toCheck.keywords, thesis.keywords),
                                percentageSimilarity=percentageSimilarity)
        commit()
        # with db_session:
        if percentageSimilarity > 90:
            winnowing_result = [(0, 0), (int(0.9 *  len(self.__toCheck.text)), int(0.9 * len(thesis.text)))]
        for i in range(0, len(winnowing_result) - 1, 1):
            index1Start = winnowing_result[i][0]
            if index1Start > winnowing_result[i + 1][0]:
                index1Start = winnowing_result[i + 1][0]
                index1End = winnowing_result[i][0]
            else:
                index1End = winnowing_result[i + 1][0]


            index2Start = winnowing_result[i][1]
            if index2Start > winnowing_result[i + 1][1]:
                index2Start = winnowing_result[i + 1][1]
                index2End = winnowing_result[i][1]
            else:
                index2End = winnowing_result[i + 1][1]

            linesWord = LinesWords(thesis1CharStart=index1Start,
                                    thesis1CharEnd=index1End,
                                    thesis2CharStart=index2Start,
                                    thesis2CharEnd=index2End,
                                    similarity = similarity)
            similarity.linesWords.add(linesWord)
            lines.append(linesWord.to_dict())
            commit()
        return {
            'thesis': similarity.thesis1.id,
            'thesis2': similarity.thesis2.id,
            'linesword': lines,
            'keywordSimilarity': similarity.keywordSimilarity,
            'percentageSimilarity': similarity.percentageSimilarity,}



    @db_session
    def process(self, toCheck):
        self.__toCheck = toCheck
        theses = Thesis.select(lambda ti: ti.id != toCheck.id)[:]
        result = {'thesis_id': toCheck.id, 'similarity': []}
        # thesisToAnalyze = []
        # for thesiin thesis:
        #     thesis= thesis.to_dict(with_collections=True, related_objects=True)
        #     # if calculate_keywords_similarity(thesis['keywords'], toCheck['keywords']) > 0.3:
        #     thesisToAnalyze.append(thesis
        pool = mp.Pool(processes=4)
        result['similarity'] = pool.map(self.process_one, theses)
        # for thesis in theses:
        #     result['similarity'].append(self.process_one(thesis))

        return result



