from dataclasses import dataclass


class NumberA:
    def __init__(self, value):
        self.value = value

    def __repr__(self): #gdy nie mam tej metody to print(a1) daje  <__main__.A object at 0x7ff211370588>
        return str(self.value)

    def __eq__(self, other): #gdy nie mam tej metody to print(a1 > a2) #daje brzydki error pypeError: '>' not supported between instances of 'A' and 'A'
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

print('klasa A (bez dekoratora @dataclass)')

a1 = NumberA(1)
print(a1.value)
print(a1)
a2 = NumberA(12)

print(a1 == a2)
print(a1 > a2)
print(a2 > a1)

print('klasa B (z dekoratorem @dataclass)')

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




@dataclass(order=True)
class Person:
    name: str
    age: int = 0

p1 = Person('Tomek',10)
p2 = Person('Ania',20)

print("Wyrażenia listowe")


print("zapis w pętli")
result=[]
for i in range(1,5):
    result.append(i**2)

print(result)
print("zapis w wyrażeniu listowym")
result = [i**2 for i in range(1,5)] #to samo co powyżej w pętli tylko krócej zapisane
print(result)

print("losujemy 5 cyfr w wyrażeniu listowym")
import random
result = [random.randint(1,10)**2 for _ in range(1,5)]
print(result)


print("losujemy 10 obiektów klasy NumsberB w wyrażeniu listowym (rzutujemy wylosowane liczby na klasę NumberB)")
a = [NumberB(random.randint(1,10)) for _ in range(1,10)]
print(a)

print("sortujemy sobie nasze obiekty")
sorted_a=sorted(a)
print(sorted_a)
reversed_sorted_a=sorted(a, reverse=True) #dzięki temu że użyliśmy @dataclass to mamy zaimplementowane juz sortowanie
print(reversed_sorted_a)


print("Można wlaczać/wylączać poszczególne metody dataclass")
@dataclass(init=True, repr=True, eq=False, order=False, frozen=False)
class C:
    pass

@dataclass(repr=False, eq=True)
class NumberC:
    value: int

a = NumberC(1)
print(a) #wylączona
b = NumberC(2)
c = NumberC(3)
print(a==b) #właczona