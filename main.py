from dotenv import load_dotenv
from abc import ABC,abstractmethod
from apis.authentication import Authentication

load_dotenv()


class Main(ABC):
    @abstractmethod
    def Run():
        auth=Authentication()
        authResult=auth.LoginUser("sbulduk","Sbulduk2023!")
        if(authResult['success']==True):
            print(f"Login Successful")
            print(f"Access Token: {authResult['access_token']}")
        else:
            print(f"Login Failed")
            print(f"Message: {authResult['message']}")

        # auth=Authentication("sbulduk","Sbulduk2023!")
        # if(auth.LoginUser()):
        #     print("Login Successful")
        # else:
        #     print("Login Failed")

if(__name__=="__main__"):
    Main.Run()