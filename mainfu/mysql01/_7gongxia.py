import threading
import time

num = 100

def show():
    global num
    time.sleep(1)
    num -=1


list = []

for i in range(100):
    t = threading.Thread(target=show)
    t.start()
    list.append(t)


    


for t in list:
    t.join()
print(num)
