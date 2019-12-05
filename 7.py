a = 5
b = 5
print(a)
print(id(a))
print(id(b))

g = 20
print(id(g))

a=10
print(id(a))

l1 = [1,2]
l2 = [1,2]
l3 = l1
l4 = l1.copy()
print(l4 is l1, 'l4 l1?')
print(l1 == l2)
print(id(l1))
print(id(l2))
l1 = [1,2,3]
print(l3)

from copy import deepcopy

my_dict = {'a': [1,2,3], 'b': [4,5,6]}
my_copy = my_dict.copy()

print(id(my_dict))
print(id(my_copy))

my_dict['a'].append(5)
print(my_dict)
print(my_copy)

# deepcopy z biblioteki copy
my_copy2 = deepcopy(my_dict)
print(my_dict)
print(my_copy2)
my_dict['a'].append('hello')
print(my_copy2)

# typy zmienne jako domyślne wartości parametrów funkcji

def add_employee(emp, emp_list = []):
    emp_list.append(emp)
    print(emp)

emps = ['Ania', 'Ola']
add_employee("A", emps)
add_employee("Staszek")
add_employee("Mgada")
add_employee("Igor")

print(emps)
