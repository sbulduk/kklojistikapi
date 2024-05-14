from apis.initvalues import InitValues
from apis.clientprocess.clientpayload import ClientPayload
from typing import Union,Dict
import requests

class Client(object):
    def __init__(self)->None:
        self.apiBaseUrl=InitValues().apiBaseUrl

    def NewClient(self,payload:ClientPayload)->Union[Dict,None]:
        newClientEndpoint=f"{self.apiBaseUrl}/api/integrator/post"
        try:
            response=requests.post(newClientEndpoint,json=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"An error occured: {e}")
            return None