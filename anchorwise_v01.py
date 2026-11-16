from anchorwise_save import create_vessel_profile
from anchorwise_load import load_vessel_profile

print("Welcome, would you like to: ")
print("Create a vessel profile? Press 1")
print("Load a saved vessel? Press 2")
chosen_option=input()
chosen_option=int(chosen_option)

if chosen_option == 1:
    print("Creating Vessel Profile: ")
    create_vessel_profile()

elif chosen_option == 2:
    print("Loading Vessel Profile: ")
    load_vessel_profile()

else:
   print("Invalid Selection")