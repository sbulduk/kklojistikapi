from dotenv import load_dotenv
import os

class InitValues(object):
    def __init__(self):
        load_dotenv()
        self.kkApiBaseUrl=os.getenv("KK_API_BASE_URL")