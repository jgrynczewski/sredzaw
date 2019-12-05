print(3*[1,2,3])
print(3*'abc')

def suma(a, b):
    return a + b

print(suma(1,2))

def my_sum(my_interegs):
    result = 0
    for item in my_interegs:
        result += item
    return result

list_of_integers = range(1000)
print(my_sum(list_of_integers())

# *args - pozycyjne argumenty wariadyczne

# f()
# f(1)
# f(1, 2)
# f(1,2,3)
#
# def f(*args):
#     print(args)
#
# f()
# f(1)

def my_sum(*args):
    return sum(list(args))

print(my_sum())
print(my_sum(1))
print(my_sum(1, 2))
