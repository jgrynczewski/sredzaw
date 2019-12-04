from dataclasses import dataclass


class NumberA:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

print('klasa A (bez dekoratora)')

a1 = NumberA(1)
print(a1.value)
print(a1)
a2 = NumberA(12)

print(a1 == a2)
print(a1 > a2)
print(a2 > a1)

print('klasa B (z dekoratorem)')

@dataclass(order=True) #to samo tylko krocej
class NumberB:
    value:int =4

b1 = NumberB(1)
print(b1.value)
print(b1) #dekorator daje nam to, ze defaultowo obiekt można ładnie wyprintować, nie trzeba implementować metody specjalnej __repr__
b2 = NumberB(10)
print(b1 == b2) #dekorator i order daje nam to, ze defaultowo obiekt można ładnie wyprintować, nie trzeba implementować metod specjalnych __lt__ ...
print(b1 > b2)
print(b2 > b1)


class A:
    pass
print(dir(A))

#każda klasa ma metody specjalne defaultowo, to te z __ przed nazwą

# __lt__(self, inny)
# __le__(self, inny)
# __eq__(self, inny)
# __ne__(self, inny)
# __gt__(self, inny)
# __ge__(self, inny)
# Zależność pomiędzy operatorami i nazwami metod przedstawia się następująco:
# x < y wywołuje x.__lt__(y),
# x <= y wywołuje x.__le__(y),
# x == y wywołuje x.__eq__(y), \
# x != y oraz x <> y wywołują x.__ne__(y), \
# x > y wywołuje x.__gt__(y), \
# x >= y wywołuje x.__ge__(y).

aa1 = A()
aa2 = A()
print(aa1) #daje brzydku print <__main__.A object at 0x7ff211370588>
print(aa1 > aa2) #daje brzydki error pypeError: '>' not supported between instances of 'A' and 'A'


