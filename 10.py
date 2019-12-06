# stos (stack)

stos = [1,4,5,7,8,9]
stos.append(10)
print(stos)
print(stos.pop())

# kolejka (queue)

q = []
q.append('eat')
q.append('sleep')
q.append('code')

print(q)

# enqueue (w pythonie append) ok ale dequeue w pythonie list pop(k)) -> O(k) za duza złożoność

from collections import deque

q = deque()

q.append('eat')
q.append('sleep')
q.append('code')

print(q)
print(q.popleft())
# print(q.popleft()) -> złożoność O(1)

# opcjonalnie appendleft i pop

from queue import Queue # asynchroniczny

q = Queue()
q.put('eatttt')
q.put('drinkkkk')
print(q.get())