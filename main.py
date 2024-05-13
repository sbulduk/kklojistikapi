import sys
sys.dont_write_bytecode=True
from abc import ABC,abstractmethod
from apis.authentication import Authentication

class Main(ABC):
    @abstractmethod
    def Run():
        auth=Authentication()
        authResult=auth.LoginUser("KK_GEBRTASKIN","123")

if(__name__=="__main__"):
    Main.Run()