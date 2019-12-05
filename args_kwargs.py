def ar_kwa(**kwargs):
    result = ''
    for item in kwargs.values():
        result += str(item)

    return result

print(ar_kwa(a=6, b='szesc', d=5, cf=45, g='sad', z=30))



def func_1(a, b, *args, f=8, **kwargs):
    pass

# Rozpakowywanie kolekcji
a, b, c =(1, 2, 3)
print(a)

t = (43, 4, 5, 6)
print(*t)

a, b, *c = (1,2,3,4,5,6,7)
print(a)
print(b)
print(c)

d={'a':7, 'b':4}
print(*d)