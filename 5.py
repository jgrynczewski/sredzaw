print(3*[1,2,3])
print(3*"abc")
print((0,1)*3)


def my_sum(a, b, c=0):
    return a+b+c

print(my_sum(1,2,4))

def my_sum(my_integers):
    result = 0
    for item in my_integers:
        result += item

    return result

list_of_integers = range(1000)
print(my_sum(list_of_integers))

# *args - pozycyjne argumenty wariadyczne

def my_sum(*args):
    return sum(args)

print(my_sum())
print(my_sum(1))
print(my_sum(1,2,5,63))
print(my_sum(3.24,5.32,52,34))


# **kwargs - nazwane argumenty wariadyczne

def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, 3, a=6, d=5, cf=45, g="asd", z=30)

# Zadanie
# Napisz funkcję, która wszystkie swoje argumenty nazwane połączy w jeden string

def concatenate(*args, **kwargs):
    result = ""
    for item in kwargs.values():
        result += str(item)
    return result

print(concatenate(a="Python", b="Is", c="Greate", d='!'))

def func(a, b, *args, d=4, **kwargs):
    pass

# Rozpakowywanie kolekcji

a, b, c = (1, 2, 3)
print(a)
t = (43,4,5,6)
print(*t) # Do spradzenia

a, b, *c = (1,2,3,4,5,6,7)
print(a)
print(b)
print(c)

d = {"a":3, "b":4}

t = [1,2,3,4]

def func(a,b,c,d):
    print(f"{a} {b} {c} {d}")

func(*t)

d = {"a":1, "b":2}

def func(**kwargs):
    print(kwargs)

func(**d)

l = [1,53,3,6]

d = {"reverse": True}

print(sorted(l, reverse=True))
print(sorted(l, **d))

d1 = {"sep": "aa"}

print('asd', 'qwe', **d1)