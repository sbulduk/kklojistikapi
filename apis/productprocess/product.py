from apis.initvalues import InitValues
from apis.productprocess.productpayload import ProductPayload
from typing import Union,Dict
import requests

class Product(object):
    def __init__(self)->None:
        self.apiBaseUrl=InitValues().apiBaseUrl

    def NewProduct(self,payload:ProductPayload)->Union[Dict,None]:
        newProductEndpoint=f"{self.apiBaseUrl}/api/integrator/post?"

        try:
            response=requests.post(newProductEndpoint,json=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"An error occured: {e}")
            return None