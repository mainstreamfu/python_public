import threading
import time

def run(n):
    print('th:',n,threading.current_thread())
    time.sleep(2)

start_time = time.time()

t_list = []
for i in range(50):
    t = threading.Thread(target=run,args=('t_%d'%i,))
    t.start()
    t_list.append(t)
print("cost time:",time.time()-start_time)
print(threading.active_count())
for i in t_list:
    t.join()

print('cost time:',time.time()-start_time,threading.current_thread())