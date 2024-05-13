from dataclasses import dataclass

@dataclass
class Communication(object):
    CommunicationTypeCode:int
    CommAddress:str