import requests
import json



#https://reqres.in/ ---- My url to refer for api



class Apitesting():

    def ApiStatusCode(self, apiType, url, body):

        if apiType=="GET":
            statusCode = requests.get(url, headers=None).status_code

        elif apiType=="POST":
            statusCode = requests.post(url, body,  headers=None).status_code

        elif apiType=="PUT":
            statusCode = requests.put(url, body,  headers=None).status_code

        else:
            print "Invalid API TYPE"
            raise Exception



        return statusCode



    def ApiResponseCode(self, apiType, url, body=None):

        if apiType == "GET":
            response = requests.get(url, headers=None).json()

        elif apiType == "POST":
            response = requests.post(url, body,headers=None).json()

        elif apiType == "PUT":
            response = requests.put(url, body,headers=None).json()

        else:
            print "Invalid"

        return response




    # def ApiTesting(self):
    #     url = "https://reqres.in/api/unknown"
    #     response = requests.get(url,headers=None).json()
    #     status_code = requests.get(url,headers=None).status_code
    #
    #
    #     print status_code
    #     print response



# c=Apitesting()
# url = "https://reqres.in/api/users"
# c.ApiTesting()
# c.ApiStatusCode("GET",url,None)
