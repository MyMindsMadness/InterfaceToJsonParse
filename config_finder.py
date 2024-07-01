import json

with open ('output.json', 'r') as f:
    data = json.load(f)


for interface in data["interface"]:
    for key, value in data["interface"][interface].items():
        if key == "ip helper" and "10.1.1.1" in value:
            print (interface)
            print (f" ip helper-address {value}")