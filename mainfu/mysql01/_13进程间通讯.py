from multiprocessing import Process,Queue,Manager,Pipe

# def start(name):
#     time.sleep(1)
#     print('hello',name)
#
#
# if __name__ == '__main__':
#     p = Process(target=start,args=('zhangsan',))
#     p1 = Process(target=start,args=('lisi',))
#
#     p.start()
#     p1.start()
#     p.join()
#

# def start(q):
#     q.put('hello')
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=start,args=(q,))
#     p.start()
#     print(q.get())
#     p.join()

# def foo(i):
#     print('say hi',i)
#
# if __name__ == '__main__ ':
#     for i in range(10):
#         p = Process(target=foo,args=(i,))
#         p.start()

import os

def f(d,l):
    d[os.getpid()]=os.getpid()
    l.append(os.getpid())
    print(l)

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(5))
        p_list = []

        for i in range(10):
            p = Process(target=f,args=(d,l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()
        print(d)
        print(l)


def start(conn):
    conn.send('hello')
    print(conn.recy())
    conn.close()

if __name__ == '__main__':
    parent_conn,child_conn = Pipe()
    p = Process(target=start,args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    parent_conn.send('12121212')
    p.join()

    #Manager(实现了进程间的真正数据共享)


