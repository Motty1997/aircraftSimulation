class Weather:
    def __init__(self , main , all , speed , dt_text):
        self.main = main
        self.all = all
        self.speed = speed
        self.dt_text = dt_text

    def __repr__(self):
        return f"main: {self.main}, all: {self.all} , speed: {self.speed} , dt_text: {self.dt_text}"