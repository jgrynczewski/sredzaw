print('wyrażenia generatora (generator expression)')


#kiedy korzystamy z listy, to zajmujemy pamięć (przy dużych listach ma to duze znaczenie)
my_list = [1,2,3]
print([x**2 for x in my_list])


#kiedy korzystamy z generatora,  nie zajmujemy pamięci na przechowywanie całej kolekcji (to główna zaleta, po to ich używamy), a efekt działania taki sam
for item in (x**2 for x in my_list):
    print(item)



#ZADANIE: suma kwadratów obiektu r za pomocą generator expression
r = range(20)
summary= 0
for item in (x**2 for x in r):
    summary +=item
print(summary)

#prościej za pomocą wyrażenia
print(sum(x**2 for x in r))

#stosuj wyrażenia listowe wtedy, jak chcesz dostać nowa listę wygenerowaną na podstawie poprzedniej

#przykłady geenratorów (funkcji zwracających itratory): range, reduce
