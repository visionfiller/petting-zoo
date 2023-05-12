class SnakePit:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "stupendous snakes of all sizes"
        self.animals = list()
    def add_animal(self,animal):
        self.animals.append(animal)