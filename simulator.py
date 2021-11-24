import json
from Drop_Class import *

def config_creator(filename):
    with open(filename, 'r') as openfile:
        json_object = json.load(openfile)
    return json_object



config1 = config_creator('config_d1513d4a-4d76-11ec-ae24-a4bb6d6e7ab9.json')
print(config1)
d1 = Game(config1)
d1
