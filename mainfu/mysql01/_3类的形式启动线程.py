import threading

class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n = n

    def run(self):
        print('run thread',self.n)

t1 = MyThread('tt1')
t2 = MyThread('tt2')

t1.start()
t2.start()