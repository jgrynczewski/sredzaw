a, b, c = (1, 2, 3)
print(a)
print(b)
print(c)

#rozpakowywanie krotki
t = (43, 4, 5, 6)
print(*t)

a, b, *c = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)

a, b, *c = {"a":3, "b":4, "c":5,  'd':4}
d = {"a":3, "b":4, "c":5, 'd':4}
print(*d)
print(a)
print(b)
print(c)


def f(**kwargs):
    for k in kwargs:
        print(k)

print('wypakowanie słownika')
print(f(**d))