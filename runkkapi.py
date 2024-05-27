from pprint import pprint
from loadpayload import Payload
from apis.karekara.authentication import Authentication
from apis.karekara.client import Client
from apis.karekara.product import Product
from apis.karekara.saleorder import SaleOrder
from apis.karekara.runproc import RunProc

class RunKKAPI(object):
    def __init__(self)->None:
        self.payload=Payload()

    def Auth(self,username:str=None,password:str=None)->str:
        auth=Authentication()
        if(username==None or password==None):
            username="KK_GEBRTASKIN"
            password="123"
        return auth.LoginUser(username,password)

    def AddNewClient(self,accessToken:str):
        newClient=Client()
        newClientPayload=self.payload.LoadJsonPayload("newclientpayload.json")
        newClientResponse=newClient.NewClient(accessToken,newClientPayload)
        pprint(f"{newClientResponse}")

    def AddNewProduct(self,accessToken:str):
        newProduct=Product()
        newProductPayload=self.payload.LoadJsonPayload("newproductpayload.json")
        newProductResponse=newProduct.NewProduct(accessToken,newProductPayload)
        pprint(f"{newProductResponse}")

    def CreateNewSaleOrder(self,accessToken:str):
        newSaleOrder=SaleOrder()
        newSaleOrderPayload=self.payload.LoadJsonPayload("newsaleorderpayload.json")
        newSaleOrderResponse=newSaleOrder.NewSaleOrder(accessToken,newSaleOrderPayload)
        pprint(f"{newSaleOrderResponse}")

    def RunNewProc(self,accessToken:str):
        runProc=RunProc()
        runProcPayload=self.payload.LoadJsonPayload("runprocpayload.json")
        runProcResponse=runProc.CallProc(accessToken,runProcPayload)
        pprint(f"{runProcResponse}")