class City:

    def __init__(self, city_name, location):
        self.city_name = city_name
        self.location = location

    def __repr__(self):
        return f"city name: {self.city_name}"