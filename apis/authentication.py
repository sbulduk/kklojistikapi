from dotenv import load_dotenv
from apis.initclient import InitClient
import os

load_dotenv()

class Authentication(object):
    def __init__(self):
        self.apiBaseUrl=os.getenv("APIBASEURL")
        self.client=InitClient.GetClient()
    
    def LoginUser(self,username,password):
        authenticationEndpoint=f"{self.apiBaseUrl}/user/authenticate"

        loginParams={
            "username":username,
            "password":password,
            "grant_type":"password"
            }
        
        try:
            response=self.client.post(authenticationEndpoint,data=loginParams)
            if(response.status_code==200):
                loginResult=response.json()
                accessToken=loginResult.get("access_token",None)
                return{
                    "success":True,
                    "message":"Login Successful",
                    "access_token":accessToken
					}
            else:
                return{
                    "success":False,
                    "message":response.text
                    }
        except Exception as e:
            return{
                "success":False,
                "message":str(e)
                }

# class Authentication(object):
#     def __init__(self,username,password)->None:
#         load_dotenv()
#         self.apiBaseUrl=os.getenv("APIBASEURL")
#         self.username=username
#         self.password=password

#     def LoginUser(self):
#         authenticationEndpoint=f"{self.apiBaseUrl}/user/authenticate"
#         loginParams={
#             "username":self.username,
#             "password":self.password,
#             "grant_type":"password"    
#         }

#         try:
#             response=requests.post(authenticationEndpoint,data=loginParams)
#             if(response.status_code==200):
#                 data=response.json()
#                 accessToken=data.get("access_token","")
#                 print(f"Access Token: {accessToken}")
#                 return {
#                     "success":True,
#                     "accessToken":data.get("access_token"),
#                     "message":response.text
#                     }
#             else:
#                 print(f"Authentication failed: {response.status_code}")
#                 print(f"Response: {response.json()}")
#                 return {
#                     "success":False,
#                     "accessToken":None,
#                     "message":response.text
#                     }
#         except requests.RequestException as re:
#             print(f"An error occurred: {str(re)}")
#             return {
#                 "success":False,
#                 "accessToken":None,
#                 "message":str(re)
#                 }

