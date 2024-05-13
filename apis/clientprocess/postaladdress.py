from dataclasses import dataclass

@dataclass
class PostalAddress(object):
    Address:str
    AddressTypeCode:str
    CountryCode:str
    StateCode:str
    CityCode:str
    DistrictCode:str