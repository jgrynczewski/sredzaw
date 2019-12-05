#isistance
#issubclass

class A:
    pass
class B(A):
    pass

a = A()
b = B()

print(isinstance(a, A)) #true
print(isinstance(b, B)) #true
print(isinstance(b, A)) #true, bo dzieciczy po rodzicach
print(isinstance(a, B)) #false
print(issubclass(B, A)) #true

#hasattr
#getattr

class C:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.c = a + b

c = C(1,2)
print(hasattr(c,'a')) #true
print(hasattr(c,'b')) #true
print(hasattr(c,'c')) #true
print(hasattr(c,'d')) #False
print(getattr(c,'c')) #3
#print(getattr(c,'d')) #error
