from abc import ABC,abstractmethod
import requests

class InitClient(ABC):
    @abstractmethod
    def GetClient():
        client=requests.Session()
        client.headers.update({
            "Accept":"application/json"
            })
        return client