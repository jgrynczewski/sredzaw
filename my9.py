print('programowanie w paradygmacie funkcyjnym')

def f(x):
    return x**2

print(f(4))

g = lambda x : x**2 #po lewej wejście po prawej wyjście
print(g(4))

#znajdź kwadraty liczb od 1 do 10 > 50

my_numbers = []
for item in range (1, 11):
    if f(item) > 50:
        my_numbers.append(item)
print(my_numbers)


#to samo tylko w 1 linii :)
# map
print(list(filter(lambda x:x**2>50, map(lambda x:x, range(1, 11)))))

def f2(x):
    return x*2
m = map(f2, [1,2,3,4])  #map  - wywołuje funkcję f2 dla każdej wartości z listy [1,2,3,4]
print(list(m)) # żeby wyprintować rzutujemy na listę
m = map(lambda x: x*2, [1,2,3,4]) #zastepujem yf2 zapisem z użyciem lambda
print(list(m))


def f3(x):
    if x % 2 == 0:
        return True
    return False

f = filter(f3, range(1,11))
print(list(f)) # żeby wyprintować rzutujemy na listę

#reduce
from functools import reduce
print(reduce(lambda x,y : x*3+y, [1, 2, 3])) #dodaje kolejne elementy, najpierw 1+2 potem do tej sumy 3 ...
print(reduce(lambda x,y: x*y, range(1,5))) # to chyba 4!


def func_pom(x):
    return x[0]**2 + x[1]**2  # odleglość punktu od srodka układu

pairs = [[1,18],[2,9],[3,8]] #macierz, albo lista punktów

print(min(pairs)) #[1,18]
print(max(pairs)) #[3,8]


print(min(pairs, key = func_pom)) # przekazujemy tu funkcję w parametrze
print(max(pairs, key = func_pom)) #

print(min(pairs, key = lambda x: x[1])) # funkcja wpisana inline
print(max(pairs, key = lambda x: x[0]**2 + x[1]**2)) # funkcja wpisana inline
