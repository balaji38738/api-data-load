import requests

class API:
    def __init__(self, url, headers=None, params=None):
        self.url = url
        self.headers = headers
        self.params = params

    def call_api(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        return response