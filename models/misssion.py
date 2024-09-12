class Mission:

    def __init__(self, target_city, priority, assigned_pilot, assigned_aircraft, distance, weather_conditions,
                 pilot_skill, aircraft_speed, fuel_capacity, mission_fit):
        self.target_city = target_city
        self.priority = priority
        self.assigned_pilot = assigned_pilot
        self.assigned_aircraft = assigned_aircraft
        self.distance = distance
        self.weather_conditions = weather_conditions
        self.pilot_skill = pilot_skill
        self.aircraft_speed = aircraft_speed
        self.fuel_capacity = fuel_capacity
        self.mission_fit = mission_fit

    def __repr__(self):
        return (f"Target_city: {self.target_city}, Priority: {self.priority}, Assigned_pilot: {self.assigned_pilot}, "
                f"assigned_aircraft: {self.assigned_aircraft}, distance: {self.distance},"
                f" weather_conditions: {self.weather_conditions}, pilot_skill: {self.pilot_skill}, "
                f"aircraft_speed: {self.aircraft_speed}, fuel_capacity: {self.fuel_capacity}, "
                f"mission_fit: {self.mission_fit}")
