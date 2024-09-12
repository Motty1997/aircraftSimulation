from city import City


class Target(City):
    def __init__(self, city_name, location, priority, weather):
        super().__init__(city_name, location)
        self.priority = priority
        self.weather = weather

    def __repr__(self):
        return f"city name: {self.city_name}, priority: {self.priority}"