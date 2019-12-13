print("Generatory -> funkcje zwracające iterator")

def my_generator():
    n=1
    print("This is first")
    yield n #zatrzymuje się i czeka na next
    n += 1
    print("This is second")
    yield n #zatrzymuje się i czeka na next
    n += 1
    print("This is third")
    yield n #zatrzymuje się i czeka na next

i = my_generator()
next(i)
next(i)
next(i)


#licznik od do
def counter(low, high):
    while low <= high:
        yield low #zatrzymuje wykonywanie funkcji i od tego meijsca rusza przy następnym wywołaniu
        low+=1
        #print('tratatata',low)

for item in counter(5,20):
    print(item)

#licznik w petli nieskończony
def counter(low):
    while True:
        yield low #zatrzymuje wykonywanie funkcji i od tego meijsca rusza przy następnym wywołaniu
        low+=1

for item in counter(5):
    print(item)



