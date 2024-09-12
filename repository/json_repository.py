import json
from models.aircraft import Aircraft
from models.pilot import Pilot
from models.city import City
from toolz import get_in
from typing import List

def read_list_aircraft_from_json(filename: str) -> List[Aircraft]:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return [Aircraft(aircraft['type'], aircraft['speed'], aircraft['fuel_capacity']) for aircraft in data]

def read_aircraft_from_json(filename: str) -> Aircraft:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return Aircraft(data['type'], data['speed'], data['fuel_capacity'])


def read_pilots_from_json(filename: str) -> List[Pilot]:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return [Pilot(pilot['name'], pilot['skill']) for pilot in data]


def read_cities_from_json(filename: str) -> List[City]:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return [City
            (get_in([0, "name"], city),
             {"let": get_in([0, "lat"], city), "lon": get_in([0, "lon"], city)}
             ) for city in data]

def read_weathers_from_json(filename: str):
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
        filt = {}
        for city, data in data.items():
            filt[city] = {"weather": get_in(["list", 0, "weather", 0, "main"], data),
                          "clouds": get_in(["list", 0, "clouds", "all"], data),
                          "wind": get_in(["list", 0, "wind", "speed"], data),
                          "dt_txt": get_in(["list", 0, "dt_txt"], data)}
    return filt

