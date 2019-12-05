# funkcje anonimowe - funkcje lambda

def f(x):
    return x**2

print(f(4))


# funkcja anonimowa
g = lambda x : x**2
print(g(4))

print(list(filter(lambda x:x**2>50, map(lambda x:x, range(1, 11)))))

'''
my_number = []
for item in range(1, 11):
    if f(item) > 50:
        my_numbers.append(item)
print(my_numbers)
'''

#map
def f2(x):
    return x*2

print(list(map(f2, [1, 2, 3, 4])))

print(list(map(lambda x:x*2, [1, 2, 3, 4])))

#filter

def f3(x):
    if x%2 == 0:
        return True
    return False

print(list(filter(f3,range(1,11))))

#reduce

from functools import reduce

print(reduce(lambda x,y : 3*x+y, [1,2,3]))

print(reduce(lambda x,y : 3*x+y, ['Jan Kowalski', '']))

# silnia

print(reduce(lambda x,y: x*y, range(1,5)))

def func_pomocnicza(x):
    return x[1]

def func_pomocnicza_2(x):
    return x[0]**2+x[1]**2

pairs = [[1, 18], [2, 9], [3, 8]]
print(min(pairs))
print(max(pairs))

print(min(pairs, key = func_pomocnicza))
print(max(pairs, key = func_pomocnicza))

print(min(pairs, key = lambda x: x[1]))
print(max(pairs, key = lambda x: x[0]**2 + x[1]**2))


