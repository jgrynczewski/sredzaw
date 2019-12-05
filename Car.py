# Zadanie 1
# Utwórz namedtuple o nazwie Car i parametrach: marka, model, liczba drzwi
# Utwórz kilka przykładów samochodu używając namedtuple Car
# Powtórz to samo używając dataclass

from collections import namedtuple
from dataclasses import dataclass

CarNamedTuple = namedtuple(("Car","marka model liczba_drzwi"))


car1 = CarNamedTuple ("nissan","kaszkaj",5)
car2 = CarNamedTuple ("toyota","yaris",5)
car3 = CarNamedTuple ("audi","a4",5)

@dataclass
class CarDataClass:
    marka: str
    model: str
    liczba_drzwi: int

car1 = CarDataClass("nissan","kaszkaj",5)
car2 = CarDataClass("toyota","yaris",5)
car3 = CarDataClass("audi","a4",5)





