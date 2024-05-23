from apis.karekara.initvalues import InitValues
from typing import Union,Dict
import requests
import json

class SaleOrder(object):
    def __init__(self)->None:
        self.apiBaseUrl=InitValues().apiBaseUrl

    def NewSaleOrder(self,accessToken:str,saleOrderPayload:str)->Union[Dict,None]:
        newSaleOrderEndpoint=f"{self.apiBaseUrl}/integrator/post"
        saleOrderHeaders={
            "Content-Type":"application/json",
            "Authorization":f"Bearer {accessToken}"
            }
        try:
            response=requests.post(newSaleOrderEndpoint,headers=saleOrderHeaders,data=json.dumps(saleOrderPayload))
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"An error occured: {e}")
            return None