import queue

q = queue.Queue()

q.put('a')
q.put(123)
print(q.qsize())

print(q.get())
