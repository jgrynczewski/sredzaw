'''Zadanie 1
Utwórz namedtuple o nazwie Car i parametrach: marka, model, liczba drzwi
Utwórz kilka przykładów samochodu używając namedtuple Car
Powtórz to samo używając dataclass'''

from collections import namedtuple

Car = namedtuple('Car', 'marka model liczba_drzwi')
my_car1 = Car('BMW', 'V6', 5)
my_car2 = Car('Volkswagen', 'Up', 3)
print(my_car1)
print(my_car1.liczba_drzwi)

from dataclasses import dataclass
print('------------przez dataclass:--------------')
@dataclass
class Car:
    marka: str
    model: str
    liczba_drzwi: int

my_car1 = Car('Volkswagen', 'Up', 3)
print(my_car1.marka)
print(my_car1)
print('------------repr klasy:-------------------')
class A:
    def __repr__(self):
        return 'blablabla' #tu musi byc string, jak np obliczenie to str(...)

a = A()
print(a)#wyswietla sie jaki object i w jakim adresie pamieci. trzeba uzyc met. repr
b = A()
print(a)
#-----------------------------------------------------