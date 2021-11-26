import json
from game import *
from overlord import *
__name__ == '__main__'

def config_creator(filename):
    with open(filename, 'r') as openfile:
        json_object = json.load(openfile)
    return json_object

simconfig = {
    "number_runs" : (int(input("How many times would you like to run your simulation?")) + 1)
}

# config filename: 
# config_2c311168-4d95-11ec-b5cc-a4bb6d6e7ab9.json
#

config1 = config_creator(str(input("Config filename: (include file extension)")))
o1 = Overlord(config1, simconfig)
o1.runSims()
print()
print(o1)
