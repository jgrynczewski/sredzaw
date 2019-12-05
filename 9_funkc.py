# funkcje lambda

def f(x):
    return x**2

print(f(4))

g = lambda x: x**2
print(g(4))

my_numbers = []
for item in range(1,11):
    if f(item) > 50:
        my_numbers.append(item)
print(my_numbers)
# to samo tylko uzywajac lambdy
print(list(filter(lambda x:x**2>50, map(lambda x:x, range(1,11)))))

#map

def f2(x):
    return x*2

print(list(map(f2, [1,2,3,4])))

def f3(x):
    if x % 2 == 0:
        return True
    return False


# to samo tylko prosciej
print(list(filter(f3, range(1,11))))



#reduce

from functools import reduce

print(reduce(lambda x,y : 3*x+y, [1, 2, 3]))

print(reduce(lambda x,y : x*y, [1,2,3,4,5]))

def func_pom(x):
    return x[1]


pairs = [[1,18], [2,9], [3,8]]
print(min(pairs))
print(max(pairs))
# wrzucamy pomocnicza funkcje co porownywac jako key
print(min(pairs, key=func_pom))
print(max(pairs, key=func_pom))
# min max dziala tylko po pierwszym elemencie



def func_pom2(x): # odleglosc od srodka ukladu
    return x[0]**2+x[1]**2


# nomralna vs anonimowa
print(min(pairs, key=func_pom2))
print(max(pairs, key=func_pom2))
print(min(pairs, key=lambda x: x[1]))
print(max(pairs, key=lambda x: x[0]**2 + x[1]**2))
