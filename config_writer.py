import json
import uuid
rare = 1
uncommon = 2
common = 3

config = [
    {
        "level" : 1,
        "reward" : 10,
        "ingredients" : [
            {"name" : "Ingredient 1", "weighting" : common},
            {"name" : "Ingredient 2", "weighting" : common},
            {"name" : "Ingredient 3", "weighting" : uncommon},
                         ]
        
    },
    {
        "level" : 2,
        "reward" : 20,
        "ingredients" : [
            {"name" : "Ingredient 4", "weighting" : uncommon},
            {"name" : "Ingredient 5", "weighting" : uncommon},
            {"name" : "Ingredient 6", "weighting" : rare},
                         ]
        
    },
    {
        "level" : 3,
        "reward" : 30,
        "ingredients" : [
            {"name" : "Ingredient 7", "weighting" : uncommon},
            {"name" : "Ingredient 8", "weighting" : uncommon},
            {"name" : "Ingredient 9", "weighting" : rare},
                         ]
        
    }
    
]


json_object = json.dumps(config, indent = 4)
name = "config_" + str(uuid.uuid1()) + ".json"
with open(name, "w") as outfile:
    outfile.write(json_object)
print(name + " successfully created.")
