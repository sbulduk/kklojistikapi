import sys
sys.dont_write_bytecode=True
from runkkapi import RunKKAPI
from runlisapi import RunLISAPI

class Main(object):
    def __init__(self):
        self.kkApp=RunKKAPI()
        self.lisApp=RunLISAPI()

    def RunKKApi(self):
        accessToken=self.kkApp.Auth("KK_GEBRTASKIN","123")["token"]
        self.kkApp.RunNewProc(accessToken)

    def RunLISApi(self):
        self.lisApp.Auth()

if(__name__=="__main__"):
    app=Main()
    app.RunKKApi()
    app.RunLISApi()