# Stos

stos = [1,4,5,7,8,9]
stos.append(10)
print(stos)
stos.pop()
print(stos)

# Kolejka

q = []
q.append('eat')
q.append('sleep')
q.append('code')

print(q)

# enqueue ok, ale  deque pop(k) -> O(k) za duza złożonsć

from collections import deque

q = deque()
q.append('eat')
q.append('sleep')
q.append('code')

print(q)
print(q.popleft())
print(q.popleft())
print(q.popleft())


# opcjonalnie możemy uzyć appendleft i pop

from queue import Queue

# q.popleft() == q.get()

