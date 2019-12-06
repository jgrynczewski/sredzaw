# Stwórzmy dwie listy
l1 = [1, 2]
l2 = [1, 2]

# Zobaczmy, czy są sobie równe:
# Shallow equality
print(l1==l2) # operator równości (equality)


# Są.
# A czy są tym samym obiektem?
# Użyjmy funkcji id, żeby sprawdzić, czy są zapisane w tym samym miejscu w pamięci.
print(id(l1))
print(id(l2))

# Mają różne id, a to oznacza, że zapisane są w różnych miejsach
# Do sprawdzenia tego mogliśmy użyć operatora is (który to co robi to
# właśnie porównuje id obiketów)
# Deep equality
print(l1 is l2) # operator identyczności (identity)

# OK. Skopiujmy teraz listę l1
# Jak to zrobić ?
# Można tak
l3 = l1

# Sprawdźmy czy zadziałało.
print(l3 is l1) # True

# Wynika z tego, że l3 i l1 wskazują na ten sam element w pamięci.
# Czyli jeżeli zmienimy którąkolwiek z list (l1 lub l3) zmiany zobaczymy w obydwu
# (ponieważ tak naprawdę jest to jeden obiekt, tylko że my nadaliśmy mu dwie nazwy - aliasy)

l3.append(3)
print(l1)
print(l3)

# Wobec tego, jak kopiować listy, żeby otrzymywać faktycznie nowy element, a nie tylko
# nową referencję do tego samego obiektu ?
# Mamy dwie metody:

# 1.
l4 = l1[:]
print(l4 is l1)

# 2.
l5 = l1.copy()
print(l5 is l1)

# Ok. W obu przypadkach powstały nowe obiekty.
# Niestety obie metody mają swoje ogranicznie. Nie skopiują przez wartość kolekcji
# zawierających modyfikowalne (mutable) obiekty.
# Jeżeli spróbujemy skopiować obiekt zawierający w sobie elementy modyfikowalne
# te metody skopiują sam obiekt, ale jeżeli chodzi o jego elementy, skopiowane
# zostaną do nich referencje a nie wartości.
# Na przykład.

l = [[1,2,3], [4,5,6]]
l_copy = l.copy()

print(l_copy is l) # False, czyli obiekty zapisane w innych miejscach w pamięci
print(l_copy[0] is l[0]) # True, czyli element wewnątrz jest tym samym obiektem

l_copy[0].append(10)
print(l)
print(l_copy)

# Wobec tego jak kopiować w pełni przez wartość. Tak, żeby w efekcie kopiowania powstał
# całkowicie nowy obiekt, z całkowicie nowymi elementami (ze skopiowanymi wartościami)?
# Należy użyć funkcji deepcopy z modułu copy

from copy import deepcopy

l_deep_copy = deepcopy(l)
print(l_deep_copy is l) # False, czyli obiekty zapisane w innych miejscach w pamięci
print(l_deep_copy[0] is l[0]) # False, czyli element wewnątrz też są nowymi obiektami

# W przypadku kopiowania samych referencji mówimy o płytkiej kopii
# W przypadku kopiowania wartości mówimy o głębokiej kopii

######################################################################################


my_dict = {'a': [1,2,3], 'b': [4,5,6]}
my_copy = deepcopy(my_dict)

print(id(my_dict))
print(id(my_copy))

my_dict['a'].append(5)
print(my_dict)
print(my_copy)

# Uwaga! Listy przekazywane są do funkcji za pomocą referencji. Oznacza to, że
# wewnątrz funkcji cały czas będziemy operowali na pierwotnej liście. Lista
# nie została skopiowana przez wartość.
# Bardzo łatwo o tym zapomnieć.

# Przekazywanie listy do parametrów funkcji (side effect)

my_list = [1, 2]

def add_elem(a, my_list):
    my_list.append(a)

add_elem(3, my_list)
add_elem(4, my_list)

print(my_list) # [1,2,3,4]

# Widać, że zmieniliśmy naszą pierwotną listę.
# Ten zabieg używany świadomie nazywany jest często side effect. Są to efekty uboczne działania
# naszej funkcji. Niestety, najczęściej zabieg ten jest wynikiem błędu, a nie świadomego działania.

# Kolejny przykład
def func(x, y=[]):
    y.append(x)
    return y

print(func(1)) #modyfikujemy y
print(func(2)) #modyfikujemy y
print(func(3, [])) #modyfikujemy nowy obiekt

# Funkcja, która przyjmuje listę jako argument i zmienia ją w ciele nazywama jest
# modyfikatorem (modifier), a zmiany które wprowadza efektami ubocznymi (side effects)

# Jeszcze jeden przykład
def doubleList(aList):
    for idx in range(len(aList)):
        aList[idx] = 2*aList[idx]

things = [2, 4, 5]
doubleList(things)
print(things)

# Jeszcze jeden przykład

def add_employee(emp, emp_list=[]):
    emp_list.append(emp)
    print(emp_list)

emps = ["Ania", "Ola"]

add_employee("Maciek", emps)
add_employee("Staszek")
add_employee("Magda")
add_employee("Igor")

# Identycznie w klasach. Listy przekazywane są przez referencję.

class A:
    def __init__(self, c, l):
        self.l = l
        self.c = c

    def add(self):
        self.l.append(self.c)

my_list = [1, 2, 3, 4]

b = A(5, my_list)
a = A(3, my_list)

a.add()
b.add()

print(my_list)


def func(alist):
    blist = alist.append(2)


my_list = [1,2,3,4]

my_dict = func(my_list)

print(my_list)








