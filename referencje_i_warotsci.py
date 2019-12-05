a = 5
g = 7

print(a)
print(g)

print(id(a))
print(id(g))

print(id(g)-id(a))

l1 = [1, 2]
l2 = [1, 2]
l3 = l1 #płytka kopia - kopiowanie referencji
print(id(l1))
print(id(l2))

print(l1 == l2) #porowanie plytkie przez wartość
print(l1 is l2) #porównanie przez referencję
print(l1 is l3)
