# import the python datetime module to help us create a timestamp
from swimming import Dolphin, Shark, LionFish, KoiFish, Otter
from walking import Alpaca, Llama, Goat, Wolf, Deer
from slithering import Cobra, CopperHead, Snake, Salamander, WaterSnake


roberto = Alpaca("Roberto", "alpaca", "midday")
print(f'{roberto.name} the {roberto.species} is available to pet during the {roberto.shift} shift.')