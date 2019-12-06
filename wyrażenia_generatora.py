# Wyrażenia generatora (generator expression)

my_list = [1,2,3]
print([x**2 for x in my_list])

for item in (x**2 for x in my_list):
    print(item)

r = range(20)
# # #suma kwadratow elementow objektow r za pomoca eneratora
# # suma = 0
# # for item in (x**2 for x in r):
#     suma += item
# #     print(suma)

print(sum(x**2 for x in r))