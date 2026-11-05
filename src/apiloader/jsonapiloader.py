from .api import API
from .json_file_writer import JSONFileWriter

def load_json_api(file_path, url, headers=None, params=None):
    api = API(url, headers, params)
    api_response = api.call_api()
    json_file_writer = JSONFileWriter(file_path, api_response.json())
    json_file_writer.write_json()
