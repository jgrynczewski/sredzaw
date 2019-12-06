print('Typy iterowalne')
#iterować można po liscie, zbiorze, krotce, strigu, po obiekcie typu range, innych obiektach iterowalnych

#jeśli klasa ma zaimplementowaną klasę __iter_- to jest iterowalna, funckcja iter() działa na niej

for item in "jakis tekst":
    print(item)

for item in [1,3,4,7]:
    print(item)

for item in range(10):
    print(item)


print("Protokół iteratora to: __iter__ oraz __next__")
#iterator musi mieć zaiplementowaną metode __next__, wywołujemy ją funkcją next()
lista= [1,2,3]
my_iterator = iter(lista) #funkcja iter zwraca iterator (wywołuje metodę __iter__ typu iterowalnego)
print(next(my_iterator)) #funkcja next wywołuje metodę __next__ iteratora
print(next(my_iterator))
print(next(my_iterator))
#print(next(my_iterator)) #wyjątek StopIteration


my_list = [1,2,3]
my_iterator = iter(my_list)
#iterowanie dopóki nie napotka sie wyjątku  StopIteration
while True:
    try:
        item = next(my_iterator)
        print(item)
    except StopIteration:
        break


print("Robimy swój iterator")
class MyCounter:
    def __init__(self,low, high):
        self.current= low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current-1

my_iterator = MyCounter(3,6)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
#print(next(my_iterator)) #wyjątek

my_counter = MyCounter(5,100)
#print(list(my_counter)) #wypisuje liste, ale! też ją od razu wysysa (przewija do stopiteration)

for item in my_counter:
    print('element',item) #iteruje po całej liscie
