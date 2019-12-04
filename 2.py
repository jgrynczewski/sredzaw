from dataclasses import dataclass


class Number:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)
        pass
    def __eq__(self, other):
        return self.value == other.value
    def __lt__(self, other):
        return self.value


one = Number(2)
print(one.value)
print(one)

print('-------------')

#nadpisywanie klasy
@dataclass(order=True) #ma umieć sie sam oporownywac
class Number_b:
    value:int

num = Number_b(5)
print(num.value)
print(num)

# > < >= <= ==

class A:
    pass

a1 = A()
a2 = A()
print(a1 > a2)

licz = 5

@dataclass(order=True)
class Person

a = [Number]
#-------------------------
#domyslne nazwy
dataclass(init=True, repr=True, eq=False, order=False, frozen=False)

#init  i eq  tylko

class Float:



