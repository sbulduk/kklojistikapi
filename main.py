import sys
sys.dont_write_bytecode=True
from payload import Payload
from pprint import pprint
import json
from apis.authentication import Authentication
from apis.client import Client
from apis.product import Product
from apis.saleorder import SaleOrder
from apis.runproc import RunProc

class Main(object):
    def Auth(self)->str:
        auth=Authentication()
        authResponse=self.AuthLogin(auth,"KK_GEBRTASKIN","123")
        if(authResponse):
            return authResponse["token"]
        else:
            print("Wrong credentials")

    def AuthLogin(self,auth:Authentication,username:str,password:str):
        try:
            return auth.LoginUser(username,password)
        except Exception as e:
            print(f"Login failed: {e}")
            return None

    def AddNewClient(self,accessToken:str):
        newClient=Client()
        payload=Payload()
        newClientPayload=payload.LoadJsonPayload("newclientpayload.json")
        newClientResponse=newClient.NewClient(accessToken,newClientPayload)
        if(newClientResponse):
            print(f"{newClientResponse}")
        else:
            print(f"Failed to add new client")

    def AddNewProduct(self,accessToken:str):
        newProduct=Product()
        payload=Payload()
        newProductPayload=payload.LoadJsonPayload("newproductpayload.json")
        newProductResponse=newProduct.NewProduct(accessToken,newProductPayload)
        if(newProductResponse):
            print(f"{newProductResponse}")
        else:
            print(f"Failed to add new product.")

    def CreateNewSaleOrder(self,accessToken:str):
        newSaleOrder=SaleOrder()
        payload=Payload()
        newSaleOrderPayload=payload.LoadJsonPayload("newsaleorderpayload.json")
        newSaleOrderResponse=newSaleOrder.NewSaleOrder(accessToken,newSaleOrderPayload)
        if(newSaleOrderResponse):
            print(f"{newSaleOrderResponse}")
        else:
            print(f"Failed to create new sale.")

    def RunNewProc(self,accessToken:str):
        runProc=RunProc()
        payload=Payload()
        runProcPayload=payload.LoadJsonPayload("runprocpayload.json")
        runProcResponse=runProc.CallProc(accessToken,runProcPayload)
        pprint(runProcResponse)
        if(runProcResponse):
            print(f"{runProcResponse}")
        else:
            print(f"Failed to run procedure.")

if(__name__=="__main__"):
    app=Main()
    accessToken=app.Auth()
    # print(f"--------------------------------------------------")
    app.RunNewProc(accessToken)