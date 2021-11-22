import json
import uuid
config = {
    "name" : "Potions",
    "p1" : "0.1",
    "p2" : "0.5",
    "p3" : "0.2",
    "p4" : "0.2"
}

json_object = json.dumps(config, indent = 4)
name = "config_" + str(uuid.uuid1()) + ".json"
with open(name, "w") as outfile:
    outfile.write(json_object)
print(name + " successfully created.")
