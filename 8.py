# Do dziedziczenia:
# Funkcja isinstance
# Funkcja issubclass

class A:
    pass

class B(A):
    pass

a = A()
b = B()

print(isinstance(b, A))
print(issubclass(B, A))

# Do obiektówki:
# Funkcja hasattr
# Funckja getattr

class C:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = a+b

c = C(1, 2)
print(hasattr(c, 'a'))
print(hasattr(c, 'd'))
print(getattr(c, 'c'))
# print(getattr(c, 'd'))