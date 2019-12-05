a = 5
g = 10
print(a)
print(id(a)) #identyfikator miejsca w pamięci

print("Dwa sposoby porównywania obiektów")
l1 = [1,2]
l2 = [1,2]
print(l1 == l2) #True porównuje przez wartość
print(id(l1))
print(id(l2))
print(l1 is l2) #False - porównuje przez referencję (identyfikator w pamięci)

print('kopiowanie plytkie przez referencję')
l3 = l1 #kolekcje kopiowane są przez referencję!!!!!!!!!!!!!!!!!! czyli: listy i krotki, tzw PŁYTKIE kopiowanie
print(l1 is l3) #true
l3.append(100)
print(l1 is l3)#true
print(l1 == l3)#true

#liczby też niekiedy mają te same miejsca w pamieci
a = 5
b = 5
print(id(a))
print(id(b))

l4=l1.copy()
print(id(l1))
print(id(l4))
print(l1 is l4)

my_dict = {'a': [1,2,3], 'b': [4,5,6]}
#my_copy = my_dict.copy()  #to wciąż kopiowanie płytkie, chociaż id są inne

print('kopiowanie głębokie / przez wartość')
from copy import deepcopy
my_copy = deepcopy(my_dict) #to kopiowanie głębokie


print(id(my_dict))
print(id(my_copy))

my_dict['a'].append(5)
print(my_dict)
print(my_copy)


print('typy zmienne jako domyślne watości parametrów funkcji')



def func(c, a= [1,2]):
    a.append(c)
    print(a)

func(4) #wyswietli 1,2,4
func(5) #wyswietli 1,2,4,5

def add_employee(emp, emp_list = None): #tak mniej więcej to powinno być oprogramowane -> nie inicjuj domyslen wartosci list
    if emp_list == None:
        emp_list = []
    emp_list.append(emp)
    print(emp_list)
    #print(emps)

emps = ["Ania","Ola"]
add_employee("Maciek",emps) #skopiowanie listy
add_employee("Staszek")
add_employee("Magda")
add_employee("Igor")
print(emps)


