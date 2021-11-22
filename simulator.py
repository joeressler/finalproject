import json
from Drop_Class import *

def config_creator(filename):
    with open(filename, 'r') as openfile:
        json_object = json.load(openfile)
    return json_object



config1 = config_creator('config_c011f526-4ba3-11ec-9198-a4bb6d6e7ab9.json')
print(config1)
d1 = Drop(config1)
d1
