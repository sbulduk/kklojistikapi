from apis.karekara.initvalues import InitValues
from typing import Union,Dict
import requests

class Authentication(object):
    def __init__(self):
        self.kkApiBaseUrl=InitValues().kkApiBaseUrl
    
    def LoginUser(self,username:str,password:str)->Union[Dict[str,str],None]:
        authenticationEndpoint=f"{self.kkApiBaseUrl}/user/authenticate"
        
        loginHeaders={
            "Content-Type":"application/x-www-form-urlencoded"
            }
        loginPayload={
            "username":username,
            "password":password,
            "grant_type":"password"
            }

        try:
            response=requests.post(authenticationEndpoint,headers=loginHeaders,data=loginPayload)
            response.raise_for_status()
            accessToken=response.json()["access_token"]
            if(accessToken):
                return {"username":username,"token":accessToken}
            else:
                return None
        except requests.RequestException as e:
            print(f"An error occured: {e}")
            return None