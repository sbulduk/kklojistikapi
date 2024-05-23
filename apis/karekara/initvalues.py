from dotenv import load_dotenv
import os

class InitValues(object):
    def __init__(self):
        load_dotenv()
        self.apiBaseUrl=os.getenv("APIBASEURL")