# Zadanie 1

# Utwórz namedtuple o nazwie Car i parametrach: marka, model, liczba drzwi
# Utwórz kilka przykładów samochodu używając namedtuple Car

# Powtórz to samo używając dataclass

import collections

Car = collections.namedtuple("Car", "brand model door_number")

toyota = Car(brand='Toyota', model='Supra', door_number=2)
subaru = Car(brand='Subaru', model='Impreza', door_number=4)
ford = Car(brand='Ford', model='Escort', door_number=5)

print(toyota)
print(subaru)
print(ford)

from dataclasses import dataclass

@dataclass
class Car2:
    brand: str
    model: str
    door_number: int

toyota2 = Car2('Toyota', 'Prius', 5)
ford2 = Car2('Ford', 'Orion', 4)
subaru2 = Car2('Subaru', 'Forester', 5)

print(toyota2)
print(ford2)
print(subaru2)