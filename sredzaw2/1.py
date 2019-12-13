a= 1
b =2
a,b = b,a
print(a, b) #daje 2, 1

class int(int):
    def __add__(self, other):
        return self - other #zmiana dodawania na odejmownie


#if __name__ == '__main__':
   #  a,b = input("Podaj dwie liczby").split(',') #sprytne pobieranie danych
   #  print(int(a) + int(b))


def is_isogram(word: str) ->bool:
    return len(word) == len(set(word))

def is_isogram_c(word:str) ->bool:
    return len({letter for letter in word}) == len(word)
    #return len([letter for letter in word if letter not in ???]) = len(word) #

#print(is_isogram_c('skrzynia'))

print('DEKORATORY')
from functools import lru_cache #cachuje juz raz obliczone rzeczy

@lru_cache(maxsize=1000)
def fiboncci(n: int) ->int:
    if(n in (1, 2)):
        return 1
    return fiboncci(n-2)+fiboncci(n-1)



cache = {} #bedziemy w tej zmiennej przechowywać wartość dla konkrentej pozycji iągu fibonaciego
#zmenna jest globalna, widoczna wewnątrz funkcji też

def fibonanacci2(n: int) -> int:
     if(n in (1,2)):
         return 1
     if(cache.get(n)): #spawdzamy czy n jest już w cache
         return cache[n] #bierzemy z cache
     cache[n] = fibonanacci2(n-2) + fibonanacci2(n-1) #zapisz do cache
     return cache[n]


def fibonanacci3(n: int) -> int: #w tej wersji zamast sprawdzać warunek if, łapiemy wystąpienie wyjątku KeyError
    if (n in (1, 2)):
        return 1
    try:
        return cache[n]  # bierzemy z cach
    except KeyError:
        cache[n] = fibonanacci2(n - 2) + fibonanacci2(n - 1)  # zapisz do cache
        return cache[n]


#print(fiboncci(12))
for i in range(1, int(input('Podaj element ciagu: '))+1):
    print(fibonanacci2(i))



#klasu abstrakcyjne, dekoratory, operacje na plikach

