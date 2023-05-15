# The package syntax is what allows for these clean import statements
from animals.animals import Animal
from movements import Walking, Swimming

class Otter(Animal, Walking, Swimming):

    def __init__(self, name, species, food, chip_num):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)
        # no more self.swimming = True
        ...

    def squeak(self):
        print("The otter squeaks. A lot")
    def run(self):
        print(f'{self} waddles')

    def __str__(self):
        return f'{self.name} the Otter'