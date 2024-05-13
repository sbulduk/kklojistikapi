from dotenv import load_dotenv
import os
import requests

class Authentication(object):
    def __init__(self):
        load_dotenv()
        self.apiBaseUrl=os.getenv("APIBASEURL")
    
    def LoginUser(self,username,password):
        loginParams={
            "username":username,
            "password":password,
            "grant_type":"password"
            }
        
        authenticationEndpoint=f"{self.apiBaseUrl}/user/authenticate"
        response=requests.post(authenticationEndpoint,data=loginParams)

        print(f"{authenticationEndpoint}")
        print(f"{username}")
        print(f"{password}")
        print("----------------------------------------")
        print(f"{response.status_code}")
        print(f"{response.json()}")
        accessToken=response.json()["access_token"]