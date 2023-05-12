# import the python datetime module to help us create a timestamp
from swimming import Dolphin, Shark, LionFish, KoiFish, Otter
from walking import Alpaca, Llama, Goat, Wolf, Deer
from slithering import Cobra, CopperHead, Snake, Salamander, WaterSnake
from attractions import PettingZoo, SnakePit, WetLands

varmint_village = PettingZoo("Varmint Village")
the_crevasse = SnakePit("The Crevasse")
atlantis = WetLands("Atlantis")
abraham = Alpaca("Abraham", "alpaca", "afternoon","corn nuts")
linda = Llama("Linda", "llama", "afternoon","tacos")
varmint_village.add_animal(linda)
varmint_village.add_animal(abraham)

print(f'{varmint_village.attraction_name} is where you will find {varmint_village.description}, like')
for animal in varmint_village.animals:
    print(animal)