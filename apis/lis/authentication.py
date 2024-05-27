from apis.lis.initvalues import InitValues
from typing import Union,Dict
import requests
from requests.auth import HTTPBasicAuth

class Authentication(object):
    def __init__(self):
        self.lisApiBaseUrl=InitValues().lisApiBaseUrl

    def LoginUser(self):
        authenticationEndpoint=f"{self.lisApiBaseUrl}/Auth"
        loginHeaders={
            "Content-Type":"application/json",
            "Authorization":"Basic bXZsb2g6JFdpbjJrOHIy"
        }
        loginPayload={
            "companyId":1,
            "divisionId":1,
            "departmentId":0
            }
        
        try:
            response=requests.post(authenticationEndpoint,headers=loginHeaders,json=loginPayload)
            response.raise_for_status()
            print(response.status_code)
            print(response.json())
            # accessToken=response.json()["access_token"]
        except requests.RequestException as e:
            print(f"An error occured: {e}")
            return None

    # def LoginUser(self,username:str,password:str)->Union[Dict[str,str],None]:
    #     authenticationEndpoint=f"{self.lisApiBaseUrl}/Auth"
    #     loginHeaders={
    #         "Content-Type":"application/json",
    #         "Authorization":"Basic bXZsb2g6JFdpbjJrOHIy"
    #     }
    #     loginPayload={
    #         "companyId":1,
    #         "divisionId":1,
    #         "departmentId":0
    #         }
        
    #     try:
    #         response=requests.post(authenticationEndpoint,headers=loginHeaders,json=loginPayload)
    #         response.raise_for_status()
    #         print(response.status_code)
    #         print(response.json())
    #         # accessToken=response.json()["access_token"]
    #     except requests.RequestException as e:
    #         print(f"An error occured: {e}")
    #         return None
        
