# Zadanie 1

# Utwórz namedtuple o nazwie Car i parametrach: marka, model, liczba drzwi
# Utwórz kilka przykładów samochodu używając namedtuple Car

# Powtórz to samo używając dataclass

from collections import namedtuple
from dataclasses import dataclass

Car = namedtuple('Car', 'mark model nr_doors')

small_car = Car(mark = 'Toyota', model = 'Yaris', nr_doors = 4)
print(f'Example of small car {small_car}')

big_car = Car(mark = 'Scania', model = 'S730', nr_doors = 2)
print(f'Example of big car {big_car}')

@dataclass
class Car:
    mark: str
    model: str
    nr_doors: int

small_car_2 = Car('Toyota', 'Aygo', 2)
print(f'Second example of small car {small_car_2}')

big_car_2 = Car('Mercedes', 'Actros', 2)
print(f'Second example of big car {big_car_2}')