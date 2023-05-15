from animals import Animal
from movements import Walking
# Designate Llama as a child class by adding (Animal) after the class name
class Wolf(Animal, Walking):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)