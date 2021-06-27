import json
def json_read(data):
        with open(data,"r") as json_file:
            data = json.load(json_file)
        return data