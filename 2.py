import random
from dataclasses import dataclass
import math

# print(dir(collections))

class Number:
    def __init__(self, value):
        self.value = value

# dataclass powoduje ze nie musimy miec inicjalizatora ale musimy podac typ i mozemy dodatkowo wart.domyslna
# dodatkowo ma __repr__ wbudowane wiec ladnie wyprintowuje obiekt
# porownywanie 5 operacji

@dataclass(order=True)
class Number:
    value:int=4

one = Number(1)
print(one.value)
print(one)


class NumberOrd:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

one = NumberOrd(1)
two = NumberOrd(2)
print('one == one')
print(one == one)
print('one < two')
print(one < two)


num1 = Number(1)
num2 = Number(2)

print('dataclass number 1 < 2')
print(num1<num2)

# porownanie oobiektow __gt__ __ge__ __le__ __lt__ __ne__ __eq__
# <, >, == <= >= !=

class A:
    pass

# print(dir(A))

a1 = A()
a2 = A()
# to nie wyjdzie
print('a1 A() == a2 A()')
print(a1 == a2)


@dataclass(order=True)
class Person:
    name: str
    age: int = 0

    def __eq__(self, other):
        return (self.name, self.age) == (other.name, other.age)


a = [NumberOrd(random.randint(1,10)) for i in range(10)]

print(a)
result = []
for i in range(1,11):
    result.append(i**2)
print(result)

# result = [i*2 for i in a]
print(result)


a = [NumberOrd(random.randint(1,10)) for _ in range(10)]
print(a)
sorted_a = sorted(a)
print(sorted_a)
reversed_sorted_a = sorted(a, reverse=True)
print(reversed_sorted_a)

@dataclass(init=True, repr=True, eq=False, order=False, frozen=False)
class C:
    pass

@dataclass(eq=False, repr = False)
class Number_c:
    value: int

a = Number_c(1)
print(a)
b = Number_c(2)
c = Number_c(3)
print(a==b)

@dataclass(frozen=True)
class Number_d:
    value: int=0

d = Number_d(5)
print(d)
# d.val ue = 3


class Float:
    def __init__(self, value=0):
        self.value = value
        self.process()

    def process(self):
        #rozpakowanie krotki z funkcji modf do 2 zmiennych
        self.decimal, self.integer = math.modf(self.value)



a = Float(2.2)
print(a.decimal, a.integer)


@dataclass
class FloatNumber:
    value: float = 0.0

    def __post_init__(self):
        self.decimal, self.integer = math.modf(self.value)

a = FloatNumber(2.2)
print(a.value)
print(a.integer)
print(a.decimal)

# dataclass dziedziczenie
@dataclass
class Person:
    name: str
    age: int = 0

@dataclass
class Student(Person):
    grade: int = 0

s = Student(20, "John", 2)
print(s.age)
print(s.name)
print(s.grade)


