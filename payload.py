import os
import json

class Payload(object):
    def __init__(self):
        self.payloadsDir=os.path.join(os.path.dirname(__file__),"payloads")

    def LoadJsonPayload(self,payloadFileName):
        with open(os.path.join(self.payloadsDir,payloadFileName),"r") as file:
            return json.load(file)