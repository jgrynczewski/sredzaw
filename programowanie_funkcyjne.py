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
