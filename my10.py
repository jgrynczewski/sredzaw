print('stos LIFO stock , push(kłądziemy do stosu) pop(zdejmujemy ze stosu), - jak w magazynie')

stos = [1,2,3,4,5,6,7,8,9]
stos.append(10) #to jest tzw push, dodanie na końcu, mała złożoność obliczeniowa, szybka operacja
last = stos.pop() #zdejmuje ostatnio dodany element, mała złożoność obliczeniowa, szybka operacja
print(last)
print(stos)




print('kolejka FIFO queue, enqueue - dodanie do kolejki, dequeue - zdjecie z kolejki, jak w sklepie') #, head - głowa, tail - ogon
q = []
q.append('eat')
q.append('seap')
q.append('code')

print(q)
print(q.pop(0)) #zdejmuje element o indeksie 2 - duża złożoność obliczeniowa (im dluższa lista tym gorzej), unikamy tego


#dodawanie(enqueue) do kolejki - OK, ale zdejmowanie(dequeue) z kolejki pop(k) ma za dużą złożoność
from collections import deque

q = deque()
q.append('eat')
q.append('seap')
q.append('code')
#aalbo od razu  (q= deque([1,2,3])

print(q)
print(q.popleft())
print(q.popleft())
print(q.popleft()) # w ten sposób znacznie wydajniej/szybciej, małą zlożoność obliczeniowas
print(q.popleft()) #zgłsza error  bo próbujemy operować na pustej kolejce
#opcjonalnie możemy użyć zestawu appendleft i pop

from queue import Queue

q = Queue()
q.put('eat')
q.put('seap')
q.put('code')

print(q)
print(q.get())
print(q.get())
print(q.get())
print(q.get()) #zawiesza się bo próbuje operować na pustej kolejce
