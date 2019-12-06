# Wyrażenia generatora (generator expression)

my_list = [1,2,3]
print([x**2 for x in my_list])
for item in (x**2 for x in my_list):
    print(item)

r = range(20)

# Suma kwadratów elementów obiektu r za pomocą generator expression.
print(sum((x**2 for x in r)))