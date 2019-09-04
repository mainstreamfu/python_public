import threading,time,queue

q = queue.Queue(maxsize=10)

def producter(pname):
    count = 1

    while True:
        q.put('数据%s'%count)
        print("[%s]生产了[数据%s]"%(pname,count))
        count += 1
        time.sleep(0.5)

def consumer(cname):
    while True:
        print("[%s]消费了[%s]" % (cname, q.get()))
        time.sleep(2)

p1 = threading.Thread(target=producter,args=("ningning",))
p1.start()

c1 = threading.Thread(target=consumer,args=("chengcheng",))

c2 = threading.Thread(target=consumer,args=("xiaoming",))

c1.start()
c2.start()

