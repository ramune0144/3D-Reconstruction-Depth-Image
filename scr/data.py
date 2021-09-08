import json
def json_read(data):
        with open(data,"r",encoding="utf8") as json_file:
            data = json.load(json_file)
        return data