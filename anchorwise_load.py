import json

def load_vessel_profile() :
    with open ("data/vessel_profile.json", "r") as file:
     boat = json.load (file)



    print(boat["name"])
    print(boat["length"])
    print(boat["keel"])
    print(boat["draft"])
    print(boat["chain"])

