from animals import Animal
from movements import Swimming

class Shark(Animal, Swimming):
    def __init__(self, name, species, food, chip_num):
            # No more super() when initializing multiple base classes
            Animal.__init__(self, name, species, food, chip_num)
            Swimming.__init__(self)