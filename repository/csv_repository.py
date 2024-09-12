import csv
from typing import List
from toolz import  pipe, partial
from models.misssion import Mission
from models.misssion import Mission

def read_people_from_csv(filepath: str) -> List[Mission]:
    try:
        with open(filepath, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            return pipe(
                [row for row in reader],
                partial(map, lambda p:
                Mission(p["target_city"], p["priority"], p["assigned_pilot"], p["assigned_aircraft"],
                        p["distance"], p["weather_conditions"], p["pilot_skill"], p["aircraft_speed"],
                        p["fuel_capacity"], p["mission_fit"]),
                list
            ))
    except Exception as e:
        print(e)
        return []



def write_person_to_csv(mission: Mission, filepath: str):
    try:
        with open(filepath, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=['target_city', 'priority', 'assigned_pilot',
                                                             'assigned_aircraft', 'distance', 'weather_conditions',
                                                            'pilot_skill', 'aircraft_speed', 'fuel_capacity',
                                                             'mission_fit'])
            csv_writer.writeheader()

            csv_writer.writerow({
                'target_city': mission.target_city,
                'age': mission.priority,
                'assigned_pilot': mission.assigned_pilot,
                'assigned_aircraft': mission.assigned_aircraft,
                'distance': mission.distance,
                'weather_conditions': mission.weather_conditions,
                'pilot_skill': mission.pilot_skill,
                'aircraft_speed': mission.aircraft_speed,
                'fuel_capacity': mission.fuel_capacity,
                'mission_fit': mission.mission_fit
            })
    except Exception as e:
        print(e)

def write_people_to_csv(missions: List[Mission], filepath: str):
    try:
        with open(filepath, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=['target_city', 'priority', 'assigned_pilot',
                                                             'assigned_aircraft', 'distance', 'weather_conditions',
                                                            'pilot_skill', 'aircraft_speed', 'fuel_capacity',
                                                             'mission_fit'])
            csv_writer.writeheader()

            for mission in missions:
                csv_writer.writerow({
                    'target_city': mission.target_city,
                    'age': mission.priority,
                    'assigned_pilot': mission.assigned_pilot,
                    'assigned_aircraft': mission.assigned_aircraft,
                    'distance': mission.distance,
                    'weather_conditions': mission.weather_conditions,
                    'pilot_skill': mission.pilot_skill,
                    'aircraft_speed': mission.aircraft_speed,
                    'fuel_capacity': mission.fuel_capacity,
                    'mission_fit': mission.mission_fit
                })
    except Exception as e:
        print(e)