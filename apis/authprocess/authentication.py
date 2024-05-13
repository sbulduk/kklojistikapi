from apis.initvalues import InitValues
from typing import Dict
import requests

class Authentication(object):
    def __init__(self):
        self.apiBaseUrl=InitValues().apiBaseUrl
    
    def LoginUser(self,username:str,password:str)->Dict[str,str]:
        loginParams={
            "username":username,
            "password":password,
            "grant_type":"password"
            }
        
        authenticationEndpoint=f"{self.apiBaseUrl}/user/authenticate"
        response=requests.post(authenticationEndpoint,data=loginParams)

        accessToken=response.json()["access_token"]
        return {"username":username,"token":accessToken}