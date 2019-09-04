#守护线程，主线程执行完了，不管守护线程有没有执行完都退出

import threading
import time

def run(n):
    print('th:',n)
    time.sleep(2)
    print(111)

start_time = time.time()

for i in range(50):
    t = threading.Thread(target=run,args=("t%d"%i,))
    t.setDaemon(True)
    t.start()

print('cost time:',time.time()-start_time)
