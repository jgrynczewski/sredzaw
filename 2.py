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

class A:
    pass
a1 = A()
a2 = A()
print(a1 == a2)#blad not supported - tzn. ze klasa A nie ma metody __gt__






