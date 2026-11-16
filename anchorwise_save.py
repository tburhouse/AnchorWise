import json

def create_vessel_profile() :
    boat_name=input("What is your boat's name? ")
    boat_length=input("What is your boat length? ")
    boat_length=float(boat_length)
    keel_type=input("What is your keel type? ")
    boat_draft=input("What is your boat draft? ")
    boat_draft=float(boat_draft)
    chain_length=input("How much chain do you have? ")
    chain_length=float(chain_length)

    if boat_length<=0:
        print("Invalid Vessel Dimensions")
    elif chain_length<0:
     print("Invalid chain lenth")
    elif boat_draft<=0:
     print("Invalid boat draft")

    else:

        boat={
        "name" : boat_name,
        "length" : boat_length,
        "keel" : keel_type,
        "draft" : boat_draft,
        "chain" : chain_length
    }

        print (boat)
    

        with open ("data/vessel_profile.json", "w") as file:
            json.dump (boat, file, indent=4)


   