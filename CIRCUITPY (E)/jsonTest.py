import json
with open('keyboard.json') as file:
    config = json.load(file)
    print(config["rows"]["row_1"])
    print(config["rows"]["row_2"])
    print(config["rows"]["row_3"])
    print(config["rows"]["row_4"])
    print(config["rows"]["row_5"])
    print(config["rows"]["row_6"])
    print(config["rows"]["row_7"])
    print(config["rows"]["send"])
