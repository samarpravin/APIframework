import json
import os
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print basedir

from LIB.Apitesting import Apitesting

filename = os.path.join(basedir + '\\CONFIG\\APICONFIG.json')
with open(filename,"r") as f:
    config_json = json.load(f)



    
class ApiFunction(Apitesting):



    def append_post_method_api_list(self):
        api_list = config_json["apitesting"]

        for k, v in api_list.items():
            if v[0] == "POST" or v[0] == "PUT":
                v.append(config_json["payload"][k])

        return api_list

    def get_all_api_response(self):
        failed_apis = []
        try:
            headers = None
            api_list = self.append_post_method_api_list()
            for apis, value in api_list.items():
                api_type, uri = value[0], "https://reqres.in"+value[1]
                print "calling api type {} and uri {}".format(api_type, uri)
                body = value[2] if len(value) > 2 else None

                response = self.ApiResponseCode(api_type, uri, json.dumps(body))
                status = self.ApiStatusCode(api_type, uri, json.dumps(body))
                print response
                print status
                if status != 200:
                    failed_apis.append(uri)
            if failed_apis:
                print "failed api {}".format(failed_apis)
                raise Exception


        except Exception, e:
            raise Exception(e)
        return failed_apis


    def call_specific_api(self,apiName):
        try:
            headers = None
            api_list = self.append_post_method_api_list()
            value = api_list[apiName]
            api_type, uri = value[0], "https://reqres.in" + value[1]
            print "calling api type {} and uri {}".format(api_type, uri)
            body = value[2] if len(value) > 2 else None
            response = self.ApiResponseCode(api_type, uri, json.dumps(body))
            status = self.ApiStatusCode(api_type, uri, json.dumps(body))
            print response
            print status
            if status != 200:
               print "api failed"
               raise Exception
        except Exception, e:
            raise Exception(e)




# c = ApiFunction()
# # c.get_all_api_response()
# c.call_specific_api("registersuccess")


