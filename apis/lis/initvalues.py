from dotenv import load_dotenv
import os

class InitValues(object):
    def __init__(self):
        load_dotenv()
        self.lisApiBaseUrl=os.getenv("LIS_API_BASE_URL")