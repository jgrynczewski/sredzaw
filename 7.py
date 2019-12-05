# l1 = [1, 2]
# l2 = [1, 2]
#
# l3 = l1
# l4 = l1[:]
#
# print(l4 is l1)
# print(id(l4))
# print(id(l1))

# l3.append(100)
# l2.append()
#
# print(l1 == l2)
# print(id(l1))
# print(id(l2))
# print(id(l3))
# print(l1 is l2)
# print(l1 is l3)
#
# print(l1)
# print(l3)
#

# print(id(a))
# print(id(b))

from copy import deepcopy

my_dict = {'a': [1,2,3], 'b': [4,5,6]}
my_copy = deepcopy(my_dict)

print(id(my_dict))
print(id(my_copy))

my_dict['a'].append(5)
print(my_dict)
print(my_copy)

# Typy zmienne jako domyślne wartości parametrów funkcji

def add_employee(emp, emp_list=[]):
    emp_list.append(emp)
    print(emp_list)

emps = ["Ania", "Ola"]

add_employee("Maciek", emps)
add_employee("Staszek")
add_employee("Magda")
add_employee("Igor")


def func(c, a=[1,2]):
    a.append(c)
    print(a)

func(4)
func(5)


# class A:
#     def __init__(self, c):
#         self.l = []
#         self.c = c
#
#     def add(self):
#         self.l.append(self.c)
# b = A(5)
# a = A(3)
#
# a.add()
# b.add()
#
# print(b.l)
# print(a.l)
