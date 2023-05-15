from animals import Animal
from movements import Walking


# Designate Llama as a child class by adding (Animal) after the class name
class Alpaca(Animal, Walking):
    
    # Remove redundant properties from Llama's initialization, and set their values via Animal
   def __init__(self, name, species, food, chip_num):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)