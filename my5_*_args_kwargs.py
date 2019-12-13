# * mnożenie
# ** potęgowanie
# import *
# multiplikowanie kolekcji
# pozycyjne argumenty wariadyczne


print("Multiplikowanie kolekcji przy użyciu *")

print(3*[1,2,3])
print(3*"abc")
print((0,1)*3)


print("Argumenty wariadyczne *args")

def summary(a, b, c = 0):
    return a + b + c

def my_sum(my_integers):
    result = 0
    for item in my_integers:
        result += item
    return result

list = range(1000)
print(my_sum(list))

def f(a=0, *args):
    print(args)

f()
f(1)
f(1,2)
f(1,2,"sdfsdf",False, None)

def my_sum(*args):
    result = 0
    for item in args:
        result += item
    return result
    #alternatywnei return sum(args)

print(my_sum())
print(my_sum(1))
print(my_sum(2,3))
print(my_sum(3.44,4.4,7.88,23.1))

print("nazwane Argumenty wariadyczne *kwargs")

def func(**kwargs):
    print(kwargs)

func(a=6,d=5,g="sdassda",z=40)

print("Połączenie argsów i kwargsów w jednej funkcji")
def func2(*args, **kwargs):
    print(args)
    print(kwargs)

func2(1,2,3, a=6,d=5,g="sdassda",z=40)


#napsz funkcje która wszystkie argumenty zwroci połączone wartosciami w jeden string
def func3(*args, **kwargs):
    result  = ''
    for item in args:
        result +=str(item)

    for item in kwargs.values():
        result +=str(item)
    return result


print(func3('zdanie',a="Python",d="is",g="great!",z=40))


def func3(a,b,*args, d=4, **kwargs): #kolejność argumentów
    pass

print('Rozpakowywanie kolekcji')

a, b, c = [1, 2, 3]
a, b, c = {1, 2, 3}
a, b, c = (1, 2, 3)
print(a) #rozpakowuje i wruca do kolejnych zmiennych.

t = (43,4,5,6)

print(*t) #rozpakowuje i rzutuje na string

a, b, *c = (1,2,3,4,5,6,7)
print(a)
print(b)
print(c)

d = {"a":3,"b":4}
print(*d) #rozpakowuje klucze



def func5(a, b, c, d):
   print(f"{a} | {b} | {c} | {d}")


t = [1,2,3,4]
func5(*t) #rozpakowujemy i przekazujemy od razu jako parametry do funkcji

def func6(**kwargs):
    print(kwargs)

e = {"a":1, "b":2}

func6(**e) #rozpakowanie slownika robimy dwoma gwiazdkami i od razu przekazujemy do funkji jako kwargsy

d1 = {"sep": "aa"}
print('asd','qwe',**d1)
