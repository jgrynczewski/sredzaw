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
a.value = 2
