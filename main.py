import sys
sys.dont_write_bytecode=True
from apis.authprocess.authentication import Authentication
from apis.clientprocess.client import Client
from apis.productprocess.product import Product

class Main(object):
    def Auth(self):
        auth=Authentication()
        authResponse=self.AuthLogin(auth,"KK_GEBRTASKIN","123")
        if(authResponse):
            uname=authResponse["username"]
            token=authResponse["token"]
            print(f"Username: {uname}")
            print(f"Token: {token}")
            print("Login successful")
        else:
            print("Wrong credentials")

    def AuthLogin(self,auth:Authentication,username:str,password:str):
        try:
            return auth.LoginUser(username,password)
        except Exception as e:
            print(f"Login failed: {e}")
            return None
        
    def AddNewClient(self):
        newClient=Client()
        newClientPayload={
            "ModelType":2,
            "CurrAccCode":"1012.1",
            "CurrAccDescription":"Musteri",
            "IdentityNum":"11111111111",
            "OfficeCode":"M",
            "WholeSalePriceGroupCode":"",
            "CreditLimit":0,
            "CurrencyCode":"TRY",
            "CustomerTypeCode":0,
            "TaxNumber":"111111111111",
            "TaxOfficeCode":"",
            "MersisNum":"111111111111",
            "IsSubjectToEShipment":True,
            "EShipmentStartDate":"2020-01-01",
            "PostalAddresses":[{
                "AddressTypeCode":"1",
                "CountryCode":"TR",
                "StateCode":"STD",
                "CityCode":"STD",
                "DistrictCode":"STD",
                "Address":"Merkez mah. Demir Sokak No:36 Şişli İstanbul"
                }
            ],
            "Communications":[{
                "CommunicationTypeCode":7,
                "CommAddress":"05555545555"
                },{
                "CommunicationTypeCode":8,
                "CommAddress":"urn:mail:despatchdefaultpk@trakyabirlik.com.tr"
                }
            ]
        }
        newClientResponse=newClient.NewClient(newClientPayload)
        if(newClientResponse):
            print(f"{newClientResponse}")
        else:
            print(f"Failed to add new client")

    def AddNewProduct(self):
        newProduct=Product()
        newProductPayload={
            "ModelType":4,
            "ItemTypeCode":"1",
            "ItemCode":"KMA0090",
            "ItemDescription":"Kareli Gömlek",
            "ItemDimTypeCode":0,
            "ItemTaxGrCode":"%8",
            "ShelfLife":20,
            "GuaranteePeriod":5,
            "ProductHierarchyID":0,
            "UsePOS":True,
            "UseStore":True,
            "UseInternet":True,
            "UnitOfMeasureCode1":"AD",
            "Attributes":[{
                "AttributeCode":"EVET",
                "AttributeTypeCode":1
                },{
                "AttributeCode":"HAYIR",
                "AttributeTypeCode":2
                },{
                "AttributeCode":"HAYIR",
                "AttributeTypeCode":3
                },{
                "AttributeCode":"HAYIR",
                "AttributeTypeCode":4
                }
            ],
            "ItemInformations":[{
                "Information":"Marka Giriniz"
                }
            ], 
            "Barcodes":[{
                "Barcode":"123",
                "BarcodeTypeCode":"Def",
                "Qty":1,
                "UnitOfMeasureCode":"AD"
                }]
            }
        newProductResponse=newProduct.NewProduct(newProductPayload)
        if(newProductResponse):
            print(f"{newProductResponse}")
        else:
            print(f"Failed to add new product.")

if(__name__=="__main__"):
    app=Main()
    app.Auth()