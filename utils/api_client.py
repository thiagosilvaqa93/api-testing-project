import requests
import os
from dotenv import load_dotenv


load_dotenv()


class APIClient:

    BASE_URL = os.getenv("BASE_URL")

    def get(self, endpoint):
        return requests.get(self.BASE_URL + endpoint)

    def post(self, endpoint, data):
        return requests.post(self.BASE_URL + endpoint, json=data)

    def put(self, endpoint, data):
        return requests.put(self.BASE_URL + endpoint, json=data)

    def delete(self, endpoint):
        return requests.delete(self.BASE_URL + endpoint)
