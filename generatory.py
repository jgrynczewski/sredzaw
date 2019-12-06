# Generatory
#
# Generat to funkcja, która zwraca iterator

def my_generator():
    n = 1
    print('This ist printed first')
    yield n

    n+=1
    print('This is printed second')
    yield n

i= iter(my_generator())
next(i)
next(i)


def counter(low, high):
    while low <= high:
        yield low
        low += 1

for item in counter(5,20):
    print(item)


#nieskończony generator
def counter_n():
    n = 0
    while True:
        n += 1
        yield n

for item in counter_n():
    print(item)
