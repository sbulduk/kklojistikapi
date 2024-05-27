from apis.karekara.initvalues import InitValues
from typing import Union,Dict
import requests
import json

class Product(object):
    def __init__(self)->None:
        self.kkApiBaseUrl=InitValues().kkApiBaseUrl

    def NewProduct(self,accessToken:str,productPayload:str)->Union[Dict,None]:
        newProductEndpoint=f"{self.kkApiBaseUrl}/integrator/post?"
        newProductHeaders={
            "Content-Type":"application/json",
            "Authorization":f"Bearer {accessToken}"
            }
        try:
            response=requests.post(newProductEndpoint,headers=newProductHeaders,data=json.dumps(productPayload))
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"An error occured: {e}")
            return None