from datetime import date

class Llama:

    def __init__(self, name, species, shift, food, chip_number):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
        self.__chip_number = chip_number
    @property # The getter
    def chip_number(self):
        return self.__chip_number

    @chip_number.setter # The setter
    def chip_number(self, number):
        pass 

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"