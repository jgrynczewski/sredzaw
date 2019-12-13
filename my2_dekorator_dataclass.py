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
@dataclass(init=True, repr=True, eq=False, order=False, frozen=True)
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
print(b)

print("frozen=True - obiekt neimodyfikowalny nie można zmieniać wartości - stałe")
@dataclass(frozen=True)
class NumberD:
    value:int = 0

a = NumberD()
print(a.value)
#a.value = 3 #niedozwolona operacja value is read only, error dataclasses.FrozenInstanceError: cannot assign to field 'value'

a = (11,12,13)
a1,a2,a3 = a #rozpakowywanie krotek, wynikiem jest a1=11, a2=12, a3=13

import math
class Float:
    def __init__(self,value=0):
        self.value = value
        self.process()

    def process(self):
        self.decimal, self.integer = math.modf(self.value)  # rozpakowanie kontenera
        # self.decimal = math.modf(self.value)[0] #to samo co powyżej tylko rozpisane
        # self.integer = math.modf(self.value)[1]

a = Float(2.2)
print(a.decimal)
print(a.integer)

@dataclass
class FloatNumber:
    value: float = 0.0

    def __post_init__(self):   #taka metoda zeby juz w momencie inicjalizacji była wwykonywana
        self.decimal, self.integer = math.modf(self.value)

print("prezentacja dziedziczenia dataclass")
@dataclass
class Person:
    name: str
    age:int = 0

    def __post_init__(self):
        print("Person A")


@dataclass
class Student(Person):
    grade: int = 0

    def __post_init__(self):
        super().__post_init__()
        print("Student B")


s= Student('name', 22, 2)
#wykonuje się post_init PErson a potem Student
print(s.name)
print(s.age)
print(s.grade)

