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