from animals import Animal
from datetime import date
from movements import Walking


# Designate Llama as a child class by adding (Animal) after the class name
class Llama(Animal, Walking):

   def __init__(self, name, species, food, chip_num):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
   def feed(self):
        print(f'on {date.today()}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}')