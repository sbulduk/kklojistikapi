from apis.karekara.initvalues import InitValues
from typing import Union,Dict
import requests
import json

class RunProc(object):
    def __init__(self):
        self.kkApiBaseUrl=InitValues().kkApiBaseUrl
    
    def CallProc(self,accessToken:str,procPayload:str)->Union[Dict,None]:
        runProcEndPoint=f"{self.kkApiBaseUrl}/integrator/runproc"
        runProcHeaders={
            "Content-Type":"application/json",
            "Authorization":f"Bearer {accessToken}"
            }
        try:
            response=requests.post(runProcEndPoint,headers=runProcHeaders,data=json.dumps(procPayload))
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"An error occured: {e}")
            return None