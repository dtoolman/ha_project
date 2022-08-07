import pandas as pd
import pgeocode
import geopy.distance
import math
import sys

# ALTERNATIVE ALGORITHM: sort the list of zipcodes based on the difference between the distance
# to hub 1 and the distance to hub 2. Specify a number (x) of zipcodes that should be assigned to 
# hub 1, and assign the first x zipcodes from the list to that hub. The remaining zipcodes go to 
# the other hub. 
# This algorithm would make it easier to modify the number of zipcodes assigned to each hub, but in
# its current state, wouldn't be able to support more than two hubs. 


# Raise an exception if location data can't be received for a zipcode
def assert_available(query):
    if math.isnan(query["latitude"]) or math.isnan(query["longitude"]):
        raise ValueError("Location data unavailable for zipcode " + str(query["postal_code"]))


nomi = pgeocode.Nominatim('us')
data = pd.read_csv("export.csv")

# Contains the names and zipcodes of all of the available hub locations
# TODO: East hub zipcode may be wrong
HUB_LOCATION_ZIPCODES = {"West": 55386, "East": 55411}

# Generate a dictionary with the coordinates of every hub location
hub_location_coords = {}
for location in HUB_LOCATION_ZIPCODES:
    query = nomi.query_postal_code(HUB_LOCATION_ZIPCODES[location])
    assert_available(query)
    hub_location_coords[location] = (query["latitude"], query["longitude"])

# Get a list of all of the unique zipcodes in the data set
unique_zipcodes = data["Address (Postal Code)"].drop_duplicates()
zipcode_corresponding_hubs = {}

for code in unique_zipcodes:
    query = nomi.query_postal_code(code)
    coords = (query["latitude"], query["longitude"])
    nearest_hub = ""
    dist_to_nearest_hub = sys.float_info.max
    for location in hub_location_coords:
        dist_to_hub = geopy.distance.geodesic(hub_location_coords[location], coords)
        if dist_to_hub < dist_to_nearest_hub:
            nearest_hub = location
            dist_to_nearest_hub = dist_to_hub
    zipcode_corresponding_hubs[code] = nearest_hub

# Create a new column in the dataset representing the serviced by the address
data["Hub"] = ""
for i, code in enumerate(data["Address (Postal Code)"]):
    data.loc[i, "Hub"] = zipcode_corresponding_hubs[code]

data.to_csv(path_or_buf="finished.csv")
