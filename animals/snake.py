from animals import Animal
from movements import Slithering

class Snake(Animal, Slithering):
    def __init__(self, name, species, food, chip_num):
            # No more super() when initializing multiple base classes
            Animal.__init__(self, name, species, food, chip_num)
            Slithering.__init__(self)