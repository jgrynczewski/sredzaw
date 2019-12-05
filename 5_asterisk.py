print(3*[1,2,3])
print(3*"abc")
print(3*(1,2,3))

def sum(arg1,arg2):
    return arg1+arg2

print(sum(1,2))



def my_sum(my_integers):
    result = 0
    for item in my_integers:
        result += item
    return result

print(my_sum([1,2,3,4,5]))
print(my_sum(range(1000)))

# *args = pozycyjne argumenty wariadyczne

def f(*args):
    print(args)

f()
f(1)
f(1,2)
f(1,2,'asd', False, None)

def g(*args):
    result = 0
    for i in args:
        result += i
    return result


print(g(1))
print(g(1,2,3,4,5))



def gg_sum(*args):
    return my_sum(args)

print(gg_sum(1,2,3,4,5))
print(gg_sum())


# kwargs - nazwane argumenty wariadyczne

def func(*args,**kwargs):
    print(args,kwargs)

print(func(1,2,3,a=6,b=4,c=5,d=1,e='asd',g=True))


# funkcja wszystkie argumenty polaczy w string

def func_string(**kwargs):
    output = ''
    for i in kwargs.values():
        output += str(i)
    print(output)

func_string(a=6, b=4, c=5, d=1, e='asd', g=True)


def g_func(a,b,*args, d=4, **kwargs):
    pass


# rozpakowywanie kolekcji, to nie sa argsy/kwargsy!!!!

a,b,c = (1,2,3)
print(a)
d,e,f = [4,5,6]
print(e)
g,h,i = {7,8,9}
print(g)
t = (43,4,5,6)
print(*t)

a,*b,c = (1,2,3,4,5,6,67,7,9)
print(b)
a,b,*c = (1,2,3,4,5,6,67,7,9)
print(c)
*a,b,c = (1,2,3,4,5,6,7,8,9)
print(a)


d = {"a":3, "b":4}
print(*d)

t = (1,2,3,4)

def func_weird(a,b,c,d):
    print(f'{a} {b} {c} {d}')

func(*t)

