# Generatory

# Generator - to funkcja zwracająca iterator

def my_generator():
    n=1
    print("This is printed first")
    yield n

    n+=1
    print("This is printed second")
    yield n

i = my_generator()
next(i)
next(i)

def counter(low, high):
    while low <= high:
        yield low
        low += 1

for item in counter(5, 20):
    print(item)

# Nieskończony generator

def my_gen():
    item = 0
    while True:
        item += 1
        yield item

for item in my_gen():
    print(item)