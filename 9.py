# Programowanie funkcyjne.

# Zgodnie z paradygmatem programowania funkcyjnego największy nacisk należy kłaść
# na stałe i funkcje.

# Podstawowe cechy paradygmatu funkcyjnego:
# * Funkcje to pojęcia podstawowe (ang. first-class)
# * Funkcje mogą operować na funkcjach (ang. high-order functions)
# * Rekurencja zamiast pętli
# * Listy jako podstawowa struktura danych
# * Brak efektów ubocznych (ang. no side-effect)
# * Wyrażenia lambda (funkcje anonimowe)
# * Leniwe wartościowanie (ang. lazy evaluation)
# * Strażnicy (ang. guards)

# Python językiem funkcyjnym nie jest, ale dostarcza takie narzędzia jak
# funkcje lambda oraz funkcje map, filter, reduce. Używanie tych funkcji
# najczęściej prowadzi do eliminacji pętli. Równie ważne są
# iteratory oraz generatory dostępne w modułach biblioteki standardowej
# takich jak itertools i functools

# Mapowanie polega na pobieraniu funkcji oraz obiektu pozwalającego na iterację
# (iterowalnego) i wygenerowaniu nowego elemenetu iterowalnego, w którym każdy
# element będzie wynikiem wywołania funkcji względem odpowiadającego mu elementu
# w początkowym obiekcie.

# Filtrowanie pozwala na iterację i wygenerowanie nowego obiektu pozwalającego na iterację,
# w którym każdy element pochodzi z początkowej sekwencji - pod warunkiem, że funkcja
# wywołana na tym elemencie zwróciła wartość True

# Redukcja polega na pobieraniu funkcji dwuargumentowej i obiektu pozwalającego na
# iterację, a następnie wygenerowaniu pojedynczej wartości z kolejnch argumentów, np:
# functools.reduce(lambda x,y: x*y, [1,2,3,4]) -> wynik 24

# Funkcje lambda
#
# Napiszmy prostę funkcję, która zwróci argument podniesiony do kwadratu.
def f(x):
    return x**2
print(f(4))

# To samo możemy zrobić za pomocą funkcji lambda
# Składnia funkcji anonimowych
g = lambda x : x**2
print(g(4))

# Po co?
# Czasami chcemy po prostu użyć funkcji raz i jej nazwa nie jest nam
# do niczego potrzebna. W powyższym przykładzie potrzebowaliśmy nazwy,
# więc nadaliśmy naszej funkcji lambda nazwę (g). Za chwilę zobaczymy przypadki,
# w których nazwa nie będzie nam do niczego potrzebna.

# Zróbmy zadanie

# Znajdź kwadrat liczb naturalnych od 1 do 10 o wartościach większych od 50.
# Zróbmy standardowo

def f(x):
    return x**2

my_numbers = []
for item in range(1,11):
    if f(item) > 50:
        my_numbers.append(item)
print(my_numbers)

# Ale możemy to zrobić również za pomocą funkcji filter i map, bez zaśmiecania przestrzeni
# nazw zbędnymi nazwami
print(list(filter(lambda x:x**2>50, map(lambda x:x, range(1, 11)))))

# Po koleji, co tu się stało.

# Funkcja map - bierze funkcję i stosuje ją do każdego typu iterowalnego.
# Przykład

def f2(x):
    return x*2

print(map(f2, [1,2,3,4]))


# Dostajemy obiekt typu map.
# Jest to typ iterowalny (możemy po nim iterować), możemy go zrzutować na inny
# typ iterowalny, np listę, która umie się ładnie wypisywać na ekranie.

print(list(map(f2, [1,2,3,4])))

# Ale nazwa f2, nie jest tu do niczego potrzebna. Usuńmy ją poprzez użycie
# funkcji anonimowej (lambda)

print(list(map(lambda x:x*2, [1,2,3,4])))

# Ok. Następna funkcja

# Funkcja filter - wybiera z typu iterowalnego elementy, które spełniają określony warunek

# Przykład, wybierzmy tylko liczby parzyste z sekwencji liczb naturalnych do 1 do 10
def f3(x):
    if x % 2 == 0:
        return True
    return False

# Funkcja przekazana do filter powinna zwracać wartość logiczną (bool)
print(filter(f3, range(1,11)))

# Tym razem dostaliśmy obiekt typu filter. Zrzutujmy go na listę.
print(list(filter(f3, range(1,11))))

# Ok, została jeszcze jedna funkcja.
# Funkcja reduce - przykłada dwuargumentową funkcję do kolejnych elementów sekwencji łącząc
# w ten sposób elementy tej sekwencji do momentu, aż zostanie jeden element.
# Przykład: Przyjmijmy, że mamy czteroelementową sekwencję:
# [1,2,3,4] i redukujemy ją funkcją x + y.
# W pierszym kroku mamy 1+2=3 -> [3, 3, 4]
# W drugim kroku mamy 3+3=6 -> [6, 4]
# W trzecim kroku mamy 6+4=10 -> 10

# Zróbmy to za pomocą funkcji reduce
from functools import reduce

print(reduce(lambda x,y: x+y, [1,2,3,4]))

# Inne przykłady
print(reduce(lambda x,y : 3*x+y , [1, 2, 3]))
print(reduce(lambda x,y: x*y, range(1,5)))

# Na koniec popatrzmy jeszcze na funkcje sorted, min, max
# Znamy już te funkcje.
# Ale do tej pory nie wspominaliśmy o opcjonalnym parametrze key, który wszystkie
# trzy mogą przyjmować. key to argument za pomocą, którego zostaną przekształcone elementy
# kolekcji na których liczymy min, max czy sorted. Funkcja min zwróci ten element
# którego wartość key(element) jest najmniejsza.
# Funkcja sorted również uporządkuje elementy według klucza.
# Domyślną wartością parametru key jest funkcja tożsamościowa (funkcja, która
# przekształca element na samego siebie).
# Przykłady

pairs = [[1, 18], [2, 9], [3, 8]]

# Domyślne zachowanie
print(min(pairs))
print(max(pairs))
# Porównywanie po pierwszy elemencie, każdej sublisty

# Z zastosowaniem zwykłych funkcji
def f(x):
    return x[1]
print(min(pairs, key=f))
print(min(pairs, key=f))

# Z zastosowaniem funkcji lambda
print(min(pairs, key=lambda x:x[1]))
print(min(pairs, key=lambda x: x[1]))

# Bardziej złożone obliczenie
print(min(pairs, key=lambda x: x[0]**2 + x[1]**2))
print(max(pairs, key=lambda x: x[0]**2 + x[1]**2))

# Identycznie z sorted
print(sorted(pairs, key=lambda x: x[0]**2 + x[1]**2))
