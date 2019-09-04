import threading

def run1():
    lock.acquire()
    global  num
    num += 1
    lock.release()
    return num


def run2():
    lock.acquire()
    global  num2
    num2 += 1
    lock.release()
    return num2

def run3():
    lock.acquire()
    res = run1()
    res2 = run2()
    lock.release()
    print(res,res2)

if __name__ == '__main__':
    num,num2 = 0,0
    lock = threading.RLock()
    for i in range(10):
        t = threading.Thread(target=run3)
        t.start()

while threading.active_count() !=1:
    pass
else:
    print(num,num2)