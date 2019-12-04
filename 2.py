from dataclasses import dataclass

class Number:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)
    def __eq__(self, other):
        return self.value == other.value
    def __lt__(self, other):
        return self.value < other.value


one = Number(1)
two = Number(2)
one = Number(1)

print(one == one)
print(one > two)
print(two < one)
print(one.value)
print(one)

@dataclass(order=True)
class NumberB:
    value: int = 4

num = NumberB(5)
print(num.value)
print(num)
num_2 = NumberB(2)
print(num_2 < num)
print(num_2 < num)
print(num < num_2)


@dataclass(order=True)
class Person:
    name: str
    age: int = 0

   # def __eq__(self, other):
    #    return (self.name, self.age) == (other.name, other.age)

import random

a = [NumberB(random.randint(1,10)) for _ in range(10)]
print(a)
sorted_a =  sorted(a)
print(sorted_a)
reversed_sorted_a = sorted(a, reverse=True)
print(reversed_sorted_a)



@dataclass(init=True, repr=True, order= False, eq = False, frozen=False )
class C:
    pass

@dataclass(repr=False, eq=True)
class NumberC:
    value: int

a = NumberC(1)
print(a)
b = NumberC(2)
b.value = 1
c = NumberC(3)
print(a == b)

@dataclass(frozen=True)
class NumberD:
    value: int = 0

a = NumberD(1)
print(a.value)
#a.value = 2

import math

class Float:
    def __init__(self, value=0):
        self.value = value
        self.process()
        #self.decimal = math.modf(self.value)
        self.decimal, self.integer = math.modf(self.value)

    def process(self):
        self.decimal, self.integer = math.modf(self.value)


a = Float(2.2)
print(a.decimal)
print(a.integer)

@dataclass
class FloatNumber:
    value: float = 0.0

    def __post_init__(self):
        self.decimal, self.integer = math.modf(self.value)

a = FloatNumber(2.2)
print(a.value)
print(a.integer)
print(a.decimal)

@dataclass
class Person:
    name: str
    age: int = 20

@dataclass
class Student(Person):
    grade: int = 0

print(type(Person))

s = Student(20, 'John', 2)
print(s.age)
print(s.name)
print(s.grade)

@dataclass
class A:
    a: int

    def __post_init__(self):
        print('A')

class B(A):
    b: int

    def __post_init__(self):
        super().__post_init__()
        print('B')

a = B(1,2)
print(a)