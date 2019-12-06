# Stos (stack)

stos = [1,4,5,7,8,9]
stos.append(10)
stos.pop()

# Kolejka (queue)

q = []
q.append('eat')
q.append('sleep')
q.append('code')

# enqueue (w Python list append) ok, ale dequeu (w Python list pop(k)) -> O(k) za duża złożoność

from collections import deque

q = deque()

q.append('eat')
q.append('sleep')
q.append('code')

print(q)

print(q.popleft())
print(q.popleft())
print(q.popleft())
# print(q.popleft()) # -> IndexError

# opcjaonalnie możemy użyć zestawu appendleft i pop

from queue import Queue

q = Queue()

q.put('eat')
q.put('sleep')
q.put('code')

print(q.get())
print(q.get())
print(q.get())
print(q.get())