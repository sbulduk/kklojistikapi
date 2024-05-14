from dataclasses import dataclass
from typing import List,Dict
from apis.clientprocess.postaladdress import PostalAddress
from apis.clientprocess.communication import Communication

@dataclass
class ClientPayload(object):
    ModelType:int
    CurrAccCode:str
    CurrAccDescription:str
    IdentityNum:str
    OfficeCode:str
    WholeSalePriceGroupCode:str
    CreditLimit:int
    CurrencyCode:str
    CustomerTypeCode:int
    TaxNumber:str
    TaxOfficeCode:str
    MersisNum:str
    IsSubjectToEShipment:bool
    EShipmentStartDate:str
    PostalAddresses:List[PostalAddress]
    Communications:List[Communication]