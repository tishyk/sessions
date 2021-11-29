import json

path = "electric_flow.json"
with open(path, encoding='utf8') as f:
    data = json.load(f)

data['project'] = "updates"

path = "new_electric_flow.json"
with open(path, 'w',  encoding='utf8') as f:
    json.dump(data, f, indent=3)

class DataLoader():
    Config_Path1 = 'data_file.json'

    def __init__(self):
        self.__dict__.update(data)

data = DataLoader()
print(data.lastName)