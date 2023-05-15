from animals import Animal
from movements import Slithering, Swimming

class Salamander(Animal, Swimming, Slithering):
    def __init__(self, name, species, food, chip_num):
            # No more super() when initializing multiple base classes
            Animal.__init__(self, name, species, food, chip_num)
            Swimming.__init__(self)
            Slithering.__init__(self)
            