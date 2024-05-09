from dotenv import load_dotenv
import os
from apis.initclient import InitClient

load_dotenv()

class ClientProcess(object):
    def __init__(self):
        self.apiBaseUrl=os.getenv("APIBASEURL")
        self.client=InitClient.GetClient()

    def CreateNewClient(self):
        newClientEndPoint=f"{self.apiBaseUrl}/Integrator/POST"

        newClientParams={
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
                },
                {
                "CommunicationTypeCode":8,
                "CommAddress":"urn:mail:despatchdefaultpk@trakyabirlik.com.tr"
                } 
            ]
            }
        
        try:
            response=self.client.post(newClientEndPoint,data=newClientParams)
            if(response.status_code==200):
                loginResult=response.json()
                return{
                    
                    }
            else:
                return{}
        except Exception as e:
            return{}

        