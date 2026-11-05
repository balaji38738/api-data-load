import json

class JSONFileWriter:
    def __init__(self, path, data):
        self.path = path
        self.data = data

    def write_json(self):
        with open(self.path, 'w') as file:
            json.dump(self.data, file)
