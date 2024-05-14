from dataclasses import dataclass
from typing import List
from apis.productprocess.attribute import Attribute
from apis.productprocess.iteminformation import ItemInformation

@dataclass
class ProductPayload(object):
    ModelType:int
    ItemTypeCode:str
    ItemCode:str
    ItemDescription:str
    ItemDimTypeCode:int
    ItemTaxGrCode:str
    ShellLife:int
    GuaranteedPeriod:int
    ProductHierarchy:int
    UsePOS:bool
    UseStore:bool
    UseInternet:bool
    UnitOfMeasureCode1:str
    Attributes:List[Attribute]
    ItemsInformations:List[ItemInformation]