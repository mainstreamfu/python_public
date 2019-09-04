import threading
import time

def test(n):
    print('thread',n)
    time.sleep(3)
    print('over')












t1 = threading.Thread(target=test,args=('tt1',))

t2 = threading.Thread(target=test,args=('tt2',))


t1.start()

t2.start()



