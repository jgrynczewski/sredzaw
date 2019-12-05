def f(x):
    return x**2
print(f(4))

g = lambda x : x**2
print(g(4))

my_numbers = []

for item in range(1,11):
    if f(item) > 50:
        my_numbers.append(item)
print(my_numbers)

print(list(filter(lambda x:x**2>50, map(lambda x:x, range(1, 11)))))

# map

#
# def f2(x):
#     return x*2

print(list(map(lambda x: x*2, [1,2,3,4])))

def f3(x):
    if x%2 == 0:
        return True
    return False

print(list(filter(f3, range(1,11))))

# reduce

from functools import reduce

print(reduce(lambda x,y : 3*x+y , [1, 2, 3]))

print(reduce(lambda x,y: x*y, range(1,5)))

pairs = [[1, 18], [2, 9], [3, 8]]


# Normalna vs anonimowa
print(min(pairs, key=lambda x: x[1]))
print(max(pairs, key=lambda x: x[0]**2 + x[1]**2))
