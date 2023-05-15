from animals import Animal
from movements import Walking


# Designate Llama as a child class by adding (Animal) after the class name
class Deer(Animal, Walking):
    def __init__(self, name, species, food, chip_num):
            # No more super() when initializing multiple base classes
            Animal.__init__(self, name, species, food, chip_num)
            Walking.__init__(self)