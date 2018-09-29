*** Settings ***
Force Tags        APIAutomation
Library           ../BIN/ApiFunction.py    WITH NAME    AC
Library           ../LIB/Apitesting.py    WITH NAME    AT
Library           requests
Library           json
Library           OperatingSystem
Library           string
Library           BuiltIn

*** Test Cases ***
Validation of all Sanity Test cases for API Framework
    AC.get_all_api_response

Validation of status and response of student_unknown API
    AC.call_specific_api    student_unknown

Validation of status and response of student_unknown2 API
    AC.call_specific_api    student_unknown2

Validation of status and response of User2 API
    AC.call_specific_api    User2

Validation of status and response of Users23 API
    AC.call_specific_api    User23

Validation of status and response of unknown23 API
    AC.call_specific_api    unknown23

Validation of status and response of users API
    AC.call_specific_api    users

Validation of status and response of registersuccess API
    AC.call_specific_api    registersuccess

Validation of status and response of registerunsuccess API
    AC.call_specific_api    registerunsuccess

Validation of status and response of loginunsuccess API
    AC.call_specific_api    loginunsuccess

Validation of status and response of users2_put API
    AC.call_specific_api    users2_put

Validation of status and response of users_delay API
    AC.call_specific_api    users_delay

Validation of status and response of loginsuccess API
    AC.call_specific_api    loginsuccess
