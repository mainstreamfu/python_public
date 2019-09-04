import threading
import time

def run(n):
    lock.acquire()
    print('th:',n)
    global num
    time.sleep(1)
    num +=1
    lock.release()
    time.sleep(2)

lock = threading.Lock()
num = 0
start_time = time.time()
for i in range(50):
    t = threading.Thread(target=run, args=("t%d" % i,))
    t.start()
print(num)
print('cost time:', time.time() - start_time)