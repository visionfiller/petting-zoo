# import the python datetime module to help us create a timestamp
from animals import Llama
from animals import Otter, Alpaca, Shark
from attractions import PettingZoo

# varmint_village = PettingZoo("Varmint Village")
# the_crevasse = SnakePit("The Crevasse")
# atlantis = WetLands("Atlantis")
# abraham = Alpaca("Abraham", "alpaca", "afternoon","corn nuts")
# linda = Llama("Linda", "llama", "afternoon","tacos",0)
# varmint_village.add_animal(linda)
# varmint_village.add_animal(abraham)

# poppy = Llama("poppy", "llama", "night", "treats", 12234)
# poppy.chip_number = 1111



# slither_inn = SnakePit("The Slither Inn")
# sammy = Cobra("Sammy", "cobra", "Ice Cube")
# shalene = Snake("Shalene", "snake", "rats...duh")
# steve = CopperHead("steve", "copperhead", "nachos")

# slither_inn.add_animal(sammy)
# slither_inn.add_animal(shalene)
# slither_inn.add_animal(steve)




# Create a Goose
bob = Otter("Bob", "Sea Otter", "watercress sandwiches", 7777)
steve= Alpaca("Steve", "alpaca", "corn", "afternoon", 1111)
dolly = Llama("Dolly", "miniature llama", "hay", 1033)
snappy = Shark("Snappy", "American Alligator", "fish", 1044)

# Create an attraction
varmint_village = PettingZoo("Varmint Village", "critters that like to dig and scurry")
varmint_village.add_animal(bob)
varmint_village.add_animal(steve)

varmint_village.add_animal_pythonic(dolly)
varmint_village.add_animal_type_check(dolly)
varmint_village.add_animal_pythonic(snappy)
for animal in varmint_village.animals:
    print(animal)

