from dataclasses import dataclass

class Number: #klasa przechowujaca liczbe
    def __init__(self, value):
        self.value = value

    def __repr__(self): #jest wywolywana przy print
        return str(self.value) #musi byc str

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value


one = Number(1)
two = Number(2)
one = Number(1)
print(one.value)
print(one)#nie dziala bez repr
print(one == one)
print(one < two)
print(two < one)

@dataclass(order=True)
class Number_b: #tu nie trzeba repr
    value:int = 4#nie znaczy to ze int jest narzucony

num = Number_b(5)
num2 = Number_b(2)
print(num.value)
print(num > num2)
print('---------------------------------------------------')

@dataclass(order=True)
class Person:
    name: str
    age: int = 0

    def __eq__(self, other): #porownanie krotek
        return (self.name, self.age) == (other.name, other.age)

@dataclass(order=True) #automatycznie
class Person:
    name: str
    age: int = 0

 #list comprehension
import random
a = [Number_b(random.randint(1,10)) for _ in range(10)] # _ - znaczy ze to tymczasowe(konwencja)
print (a)
result = []
for i in range(1, 5):
    result.append(i**2)

print (result)

result = [i**2 for i in range(1, 5)]

print (result)

#sorted()
a = [Number_b(random.randint(1,10)) for _ in range(10)] # _ - znaczy ze to tymczasowe(konwencja)
print (a)
sorted_a = sorted(a)
print(sorted_a)
reversed_sorted_a = sorted(a, reverse=True)
print(reversed_sorted_a)

@dataclass(init=True, repr=True, eq=False, order=False, frozen=False)
class C:
    pass

@dataclass(repr=False, eq=True)
class Number_c:
    value: int
    
a = Number_c(2)
c = Number_c(3)
print(a == c)

@dataclass(frozen=False)  #jak True nie mozna potem zmienic wartosci, wywala blad
class Number_d:
    value: int = 0

a = Number_d(1)
print(a.value)
a.value = 2
print(a.value)

import math
'''
class Float:
    def __init__(self, value=0):
        self.value = value
        self.process()

    def process(self):
        self.decimal, self.integer = math.modf(self.value)
        #rozpakowywanie kontenerów

a = Float(1, 1)
print (a.value) '''
@dataclass   #dziedziczenie w dataclass
class Person:
    name: str
    age: int = 0
@dataclass
class Student(Person):
    grade: int = 0

s = Student(20, 'John', 2)
print(s.name, s.age, s.grade)

#@dataclass
#class B(A)









