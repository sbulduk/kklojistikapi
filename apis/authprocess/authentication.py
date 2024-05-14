from apis.initvalues import InitValues
from typing import Union,Dict
import requests

class Authentication(object):
    def __init__(self):
        self.apiBaseUrl=InitValues().apiBaseUrl
    
    def LoginUser(self,username:str,password:str)->Union[Dict[str,str],None]:
        loginParams={
            "username":username,
            "password":password,
            "grant_type":"password"
            }
        
        authenticationEndpoint=f"{self.apiBaseUrl}/user/authenticate"

        try:
            response=requests.post(authenticationEndpoint,data=loginParams)
            response.raise_for_status()
            accessToken=response.json()["access_token"]
            if(accessToken):
                return {"username":username,"token":accessToken}
            else:
                return None
        except requests.RequestException as e:
            print(f"An error occured: {e}")
            return None