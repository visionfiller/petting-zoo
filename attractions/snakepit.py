class SnakePit:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "stupendous snakes of all sizes"
        self.animals = list()
    @property
    def last_critter_added(self):
        return f'{self.animals[-1]}'
    def add_animal(self,animal):
        self.animals.append(animal)