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
# print(one.value)
print(one == one)
print(one < two)
print(two < one)

@dataclass(order=True)
class Number_b:
    value:int = 4

num = Number_b(5)
num2 = Number_b(2)
print(num > num2)

@dataclass(order=True)
class Person:
    name : str
    age: int = 0

import random

a = [Number_b(random.randint(1,10)) for _ in range(10)]
print(a)
sorted_a = sorted(a)
print(sorted_a)
reversed_sorted_a = sorted(a, reverse=True)
print(reversed_sorted_a)

@dataclass(init=True, repr=True, eq=False, order=False, frozen=False)
class C:
    pass

@dataclass(repr = False, eq=True)
class Number_c:
    value: int

a = Number_c(1)
print(a)
b = Number_c(2)
b.value = 1
c = Number_c(3)
print(a==b)

@dataclass(frozen=True)
class Number_d:
    value: int = 0

a = Number_d(1)
print(a.value)
a.value = 2