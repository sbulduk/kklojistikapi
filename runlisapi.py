from apis.lis.authentication import Authentication

class RunLISAPI(object):
    def __init__(self):
        pass

    def Auth(self)->None:
        auth=Authentication()
        auth.LoginUser()

    # def Auth(self,username:str=None,password:str=None)->None:
    #     auth=Authentication()
    #     if(username==None or password==None):
    #         username="Sbulduk"
    #         password="Sbulduk2023!"
    #     auth.LoginUser(username,password)