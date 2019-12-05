print(3*[1,2,3])
print(3*'abc')
print((0,1)*3)

def sum(a, b, c=0):
    return a+b+c

def my_sum(my_integers):
    result = 0
    for item in my_integers:
        result += item
    return result, my_integers

list_of_integers = range(1000)
print(my_sum(list_of_integers))

# *args - pozycyjne argumenty wariadyczne. nie zakladamy z gory ile ich bedzie
def sum_args(*args):
    result = 0
    for item in args:
        result += item
    return result, len(args), result/len(args)

print(sum_args(1,2,3,4,5,6,7,8))

def f(a=0, *args):
    print(args, type(args))

f()
f(1)
f(1,2)
f(1,2,'asd', False, None)

# *kwargs - nazwane argumenty wariadyczne. Sa umieszczane w slowniku
def func(*args, **kwargs):
    print(args)
    print(kwargs)
func(1,2,3, a=6, d=5, cf=45, g='asd', z=30)

#fkcja ktora polczy w string arg nazwane do niej przekazane

def concat(*args):
    result = ''
    for item in args:
        result += str(item)
    return result
print(concat('t','y',345,'f','34u','ff',0))

def concatenate(*args, **kwargs):
    result = ''
    for item in kwargs.values():
        result += str(item)
    return result
print(concatenate(a='Python', b='Is', c='Great', d='!'))

#rozpakowywanie kolekcji
a, b, c = (1,2,3)
print(a)
a, b, *c = (12,32,45,67,4,322,45,9)
print(a)
print(b)
print(c)#wypisze cala reszte

#rozpakowanie slownika
d = {'a':3, 'b':4}
def func(**kwargs):
    print(kwargs)
func(**d)

l = [1,53,36]
d = {'reverse': True}
print(sorted(l, **d))
print(sorted(l, reverse=False))

d1 = {'sep': 'aa'} #przekazanie arg do fkcji przez rozpakowaie kolekcji
print('asd', 'qwe', **d1)