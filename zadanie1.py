# Zadanie 1

# Utwórz namedtuple o nazwie Car i parametrach: marka, model, liczba drzwi
# Utwórz kilka przykładów samochodu używając namedtuple Car

# Powtórz to samo używając dataclass

from collections import namedtuple

Car = namedtuple("Car", "marka model liczba_drzwi")

my_car_1 = Car("BMV", "V6", 5)
my_car_2 = Car("Volkswagen", "Up", 3)

print(my_car_1)
print(my_car_2.liczba_drzwi)

from dataclasses import dataclass

@dataclass
class Car:
    marka: str
    model: str
    liczba_drzwi: int

my_car_1 = Car("BMV", "V6", 5)
my_car_2 = Car("Volkswagen", "Up", 3)

print(my_car_1)
print(my_car_2.liczba_drzwi)