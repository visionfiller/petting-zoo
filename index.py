# import the python datetime module to help us create a timestamp
from swimming import Dolphin, Shark, LionFish, KoiFish, Otter
from walking import Alpaca, Llama, Goat, Wolf, Deer
from slithering import Cobra, CopperHead, Snake, Salamander, WaterSnake
from attractions import PettingZoo, SnakePit, WetLands

varmint_village = PettingZoo("Varmint Village")
the_crevasse = SnakePit("The Crevasse")
atlantis = WetLands("Atlantis")
abraham = Alpaca("Abraham", "alpaca", "afternoon","corn nuts")
linda = Llama("Linda", "llama", "afternoon","tacos",0)
varmint_village.add_animal(linda)
varmint_village.add_animal(abraham)

poppy = Llama("poppy", "llama", "night", "treats", 12234)
poppy.chip_number = 1111

print(poppy.chip_number)

slither_inn = SnakePit("The Slither Inn")
sammy = Cobra("Sammy", "cobra", "Ice Cube")
shalene = Snake("Shalene", "snake", "rats...duh")
steve = CopperHead("steve", "copperhead", "nachos")

slither_inn.add_animal(sammy)
slither_inn.add_animal(shalene)
slither_inn.add_animal(steve)

print(slither_inn.last_critter_added)
