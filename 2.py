'''
'''
from dataclasses import dataclass #wymagane przy użyciu


#defaultdict przechowują dane i reprezentują typ danych
class Number:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return  str(self.value)

    def __eq__(self, other):
        return  self.value == other.value

    def __lt__(self, other):
        return self.value < other.value


one = Number(1)
print(one.value)

two = Number(1)
print(two.value)

print(one == two)
print(one < two)
print(two < one)

#przechowuje i porównuje dane jakie zawierają obiekty klasy
@dataclass (order=True)
class NumberDC:
    value: int = 4



one_dc = NumberDC(2)
print(one_dc.value)

two_dc = NumberDC()
print(two_dc.value)
print(repr(two_dc.value))

# <, >, ==, <=, >=

a1 = Number(1)
a2 = Number(2)
print(a1 < a2)

print(one_dc < two_dc)
print(one_dc == two_dc)
print(two_dc < one_dc)

@dataclass(order=True)
class Person:
    name: str
    age: int = 0

    #def __eq__(self, other):
        #return (self.name, self.age) == (other.name, other.age)



import  random
a = [NumberDC(random.randint(1, 10)) for _ in range(10)]
print(a)
a_sorted = sorted(a)
print(a_sorted)
reversed_a= sorted(a, reverse=True)
print(reversed_a)

@dataclass(init=True, repr=True, eq=False, order=False, frozen=False)
class C:
    pass

@dataclass(eq=True, repr=False)
class Number_c:
    value: int

a = Number_c(1)
b = Number_c(2)
c= Number_c(3)
print(a)
print(a == b)

@dataclass(frozen=True)
class Number_d:
    value: int = 0

a = Number_d(1)
print(a)

import  math
class Float:
    def __init__(self, value=0):
        self.value = value
        self.process()

    def process(self):
        self.decimal, self.integer = math.modf(self.value)


#a = Float(2,2)
#print(a.decimal)
#print(a.integer)


@dataclass
class Person:
    name: str
    age: int

@dataclass
class Student(Person):
    grade: int = 0

p = Person('a',1)
s = Student('s',2,0)

print(dir(p))
print(dir(s))
print(p.name, p.age)
print(s.name, s.age, s.grade)