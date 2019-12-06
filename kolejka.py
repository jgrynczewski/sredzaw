from collections import deque
q = deque()
q.append("eat")
q.append("sleep")
q.append("code")
print(q)

print(q.popleft())
print(q)
print(q.popleft())
print(q)
print(q.popleft())

q = deque()
q.appendleft("eat")
q.appendleft("sleep")
q.appendleft("code")
print(q)

q.pop()
print(q)
q.pop()
print(q)
q.pop()
print(q)

from queue import Queue
q = Queue()
q.put("eat")
q.put("sleep")
q.put("code")

q.get()
print(q)
q.get()
print(q)