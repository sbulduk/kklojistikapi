from apis.initvalues import InitValues
from apis.clientprocess.clientpayload import ClientPayload
import requests

class Client(object):
    def __init__(self):
        self.apiBaseUrl=InitValues().apiBaseUrl

    def NewClient(self,payload:ClientPayload):
        newClientEndpoint=f"{self.apiBaseUrl}/api/integrator/post"
        response=requests.post(newClientEndpoint,json=payload.__dict__)

        return response.json()