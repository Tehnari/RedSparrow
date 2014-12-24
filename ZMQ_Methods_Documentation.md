**This documentation is automatically generated.**


# fieldofstudymethods
    JSON-RPC

**Args**

*

 * args

 * kwargs
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

Method called when JSON-RPC for __name



<br>
<br>

# fieldofstudymethods-add_thesis_to_fos
    JSON-RPC

**Args**

*

 * fosId

 * thesisId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# fieldofstudymethods-delete_fos
    JSON-RPC

**Args**

*

 * fosId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# fieldofstudymethods-edit_fos
    JSON-RPC

**Args**

*

 * columnName

 * value

 * fosId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# fieldofstudymethods-get_fos_by_id
    JSON-RPC

**Args**

*

 * fosId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# fieldofstudymethods-list_all_of_fos
    JSON-RPC

**Args**
None


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# gettext
    JSON-RPC

**Args**

*

 * args

 * kwargs
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

Method called when JSON-RPC for __name



<br>
<br>

# keywordmethods
    JSON-RPC

**Args**

*

 * args

 * kwargs
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

Method called when JSON-RPC for __name



<br>
<br>

# keywordmethods-add_thesis_to_keyword
    JSON-RPC

**Args**

*

 * kId

 * thesisId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# keywordmethods-delete_keyword
    JSON-RPC

**Args**

*

 * keyId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# keywordmethods-edit_keyword
    JSON-RPC

**Args**

*

 * columnName

 * value

 * keyId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# keywordmethods-get_keyword_by_id
    JSON-RPC

**Args**

*

 * keyId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# keywordmethods-get_keywords_by_thesis_id
    JSON-RPC

**Args**

*

 * thesisId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# keywordmethods-list_all_of_keywords
    JSON-RPC

**Args**
None


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# levelmethods
    JSON-RPC

**Args**

*

 * args

 * kwargs
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

Method called when JSON-RPC for __name



<br>
<br>

# levelmethods-add_user_to_level
    JSON-RPC

**Args**

*

 * levelId

 * userId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# levelmethods-delete_level
    JSON-RPC

**Args**

*

 * lvlId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# levelmethods-edit_level
    JSON-RPC

**Args**

*

 * columnName

 * value

 * lvlId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# levelmethods-get_level_by_id
    JSON-RPC

**Args**

*

 * lvlId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# levelmethods-get_level_by_user_id
    JSON-RPC

**Args**

*

 * userId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# levelmethods-list_all_of_levels
    JSON-RPC

**Args**
None


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# login
    JSON-RPC

**Args**

*

 * login

 * password
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

Login method

:param login: user Login

:param password: hash of password



<br>
<br>

# login-test_method
    JSON-RPC

**Args**
None


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

Ping method. It tests if server is up.



<br>
<br>

# register
    JSON-RPC

**Args**

*

 * login

 * password

 * email

 * name

 * surname
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

Register method

params - dict

:param login: user Login

:param email: user email

:param password: hash of user password

:param surname: user surname

:param name: user name

:returns: If success returns all user data else return JSON-RPC error object



<br>
<br>

# thesisdetailsmethods
    JSON-RPC

**Args**

*

 * args

 * kwargs
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

Method called when JSON-RPC for __name



<br>
<br>

# thesisdetailsmethods-delete_thesis
    JSON-RPC

**Args**

*

 * thesisDetailsId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# thesisdetailsmethods-edit_thesis_detail
    JSON-RPC

**Args**

*

 * columnName

 * value

 * detailsId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# thesisdetailsmethods-get_thesis_details_by_thesis_id
    JSON-RPC

**Args**

*

 * thesisId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# thesismethods
    JSON-RPC

**Args**

*

 * args

 * kwargs
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

Method called when JSON-RPC for __name



<br>
<br>

# thesismethods-add_thesis_to_user_by_user_id
    JSON-RPC

**Args**

*

 * userId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# thesismethods-delete_thesis
    JSON-RPC

**Args**

*

 * thesisId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# thesismethods-edit_thesis
    JSON-RPC

**Args**

*

 * columnName

 * value

 * thesisId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# thesismethods-get_list_of_thesis
    JSON-RPC

**Args**
None


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# thesismethods-get_thesis_by_keyword_id
    JSON-RPC

**Args**

*

 * keywordId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# thesismethods-get_thesis_by_title
    JSON-RPC

**Args**

*

 * query
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# thesismethods-get_thesis_by_user_id
    JSON-RPC

**Args**

*

 * userId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# thesismethods-get_thesis_list_by_fos_id
    JSON-RPC

**Args**

*

 * fosId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# thesismethods-get_thesis_list_by_thesis_status_id
    JSON-RPC

**Args**

*

 * tStatusId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# thesismethods-get_thesis_status_by_thesis_id
    JSON-RPC

**Args**

*

 * thesisId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# thesismethods-get_thesis_status_by_title
    JSON-RPC

**Args**

*

 * thesisTitle
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# thesismethods-get_thesis_text_by_thesis_id
    JSON-RPC

**Args**

*

 * id
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# thesisstatusmethods
    JSON-RPC

**Args**

*

 * args

 * kwargs
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

Method called when JSON-RPC for __name



<br>
<br>

# thesisstatusmethods-add_thesis_to_thesis_status
    JSON-RPC

**Args**

*

 * thesisStatusId

 * thesisId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# thesisstatusmethods-delete_fos
    JSON-RPC

**Args**

*

 * thesisStatusId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# thesisstatusmethods-edit_fos
    JSON-RPC

**Args**

*

 * columnName

 * value

 * thesisStatusId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# thesisstatusmethods-get_fos_by_id
    JSON-RPC

**Args**

*

 * thesisStatusId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# thesisstatusmethods-list_all_of_statuses
    JSON-RPC

**Args**
None


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# usermethods
    JSON-RPC

**Args**

*

 * args

 * kwargs
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

Method called when JSON-RPC for __name



<br>
<br>

# usermethods-add_user_level_by_user_id
    JSON-RPC

**Args**

*

 * userId

 * levelId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# usermethods-delete_user
    JSON-RPC

**Args**

*

 * userId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# usermethods-edit_user
    JSON-RPC

**Args**

*

 * columnName

 * value

 * userId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# usermethods-get_list_of_users
    JSON-RPC

**Args**
None


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# usermethods-get_user_by_id
    JSON-RPC

**Args**

*

 * userId
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# usermethods-set_email
    JSON-RPC

**Args**

*

 * value
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None



<br>
<br>

# usermethods-set_user_password_by_user_id
    JSON-RPC

**Args**

*

 * userId

 * password
            


**Input Schema**
```json

```

**Output Schema**
```json

```


**Notes**

None

