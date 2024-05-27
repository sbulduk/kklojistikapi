from apis.karekara.initvalues import InitValues
from typing import Union,Dict
import requests
import json
from pprint import pprint

class Client(object):
    def __init__(self)->None:
        self.kkApiBaseUrl=InitValues().kkApiBaseUrl

    def NewClient(self,accessToken:str,clientPayload:str)->Union[Dict,None]:
        newClientEndpoint=f"{self.kkApiBaseUrl}/integrator/post"
        newClientHeaders={
            "Content-Type":"application/json",
            "Authorization":f"Bearer {accessToken}"
            }
        try:
            response=requests.post(newClientEndpoint,headers=newClientHeaders,data=json.dumps(clientPayload))
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"An error occured: {e}")
            return None