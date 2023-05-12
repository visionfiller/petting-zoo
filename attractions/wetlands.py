
class WetLands:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "creatures of the water"
        self.animals = list()
    def add_animal(self,animal):
            self.animals.append(animal)