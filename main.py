import sys
sys.dont_write_bytecode=True
from apis.authprocess.authentication import Authentication
from apis.clientprocess.client import Client

class Main(object):
    def Auth(self):
        auth=Authentication()
        try:
            authResponse=auth.LoginUser("KK_GEBRTASKIN","123")
        except:
            authResponse=None

        if(authResponse is not None):
            print(f"Login successful")
        else:
            print("Wrong credentials")
        
    def AddNewClient(self):
        client=Client()

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

        newClientResponse=client.NewClient(newClientPayload)
        print(f"{newClientResponse}")



if(__name__=="__main__"):
    app=Main()
    app.Auth()