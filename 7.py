a = 5
g = 10
print(a)
print(id(a))
print(id(g))

l1 = [1, 2]
l2 = [1, 2]

l3 = l1
l4 = l1.copy()

print(l1 == l2) # por. przez watość
print(id(l1))
print(id(l2))
print(l1 is l2) # por. przez referencję

print(id(l3))
print(l1 == l3)
print(l1 is l3)

l3.append(100)
print(l1)

l1.append(50)
print(l3)

# kopia listy
print(l4 is l1)

my_dict = {'k': [1,2,3], 'l': [4,5,6]}
my_copy = my_dict.copy()
#my_copy_2 = deepcopy(my_dict)

print(id(my_dict))
print(id(my_copy))

my_dict['k'].append(5)
print(my_dict)
print(my_copy)

print(id(my_dict))
#print(id(my_copy_2))


#typy zmienne jako doyślne watości parametrów funkcji

def add_employee(emp, emp_list=None):
    if not emp_list:
        emp_list = []
        emp_list.append(emp)
    print(emp_list)

emps = ['Ania', 'Ola']

add_employee('Maciek', emps)
add_employee('Staszek')
add_employee('Magda')
add_employee('Igor')


def func_ref(c, a=[1,2]):
    a.append(c)
    print(a)

func_ref(4)
func_ref(5)


# class A:
#     def __init__(self c):
#         self.l = []
#     def add():
#         self.l.append(self.c)
