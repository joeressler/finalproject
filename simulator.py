import json
from game import *

def config_creator(filename):
    with open(filename, 'r') as openfile:
        json_object = json.load(openfile)
    return json_object



config1 = config_creator(
    'config_2c311168-4d95-11ec-b5cc-a4bb6d6e7ab9.json'
    )
d1 = Game(config1)
d1
