import math
from toolz import compose
from toolz.curried import partial, pluck, reduce

from repository.json_repository import *


cities = read_cities_from_json("../repository/cities_location.json")
all_aircraft = read_list_aircraft_from_json("../aircrafts.json")
all_pilots = read_pilots_from_json("../pilots.json")
all_weather = read_weathers_from_json("../repository/weather_data.json")


def weather_score (weather):
    if weather['condition'] == "Clear":
        return 1.0 # Best condition
    elif weather['condition'] == "Clouds":
        return 0.7 # clouds are moderate
    elif weather['condition'] == "Rain":
        return 0.4 # Rainy weather
    elif weather['condition'] == "Stormy":
        return 0.2 # Stormy weather is least favorable
    else:
        return 0 # Unfavorable condition


# Function to calculate the distance between two coordinates using the Haversine formula
def haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371.0 # Radius of the Earth in kilometers

    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Calculate differences between the coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Apply Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate the distance
    distance = r * c

    return distance
