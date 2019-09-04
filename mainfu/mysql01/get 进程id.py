# from multiprocessing import Process
# import os
#
# def info(title):
#     print(title)
#     print('module name:',__name__)
#     print('parent process:',os.getppid())
#     print('process id:',os.getpid())
#     print('\n')
#
# def f(name):
#     info('called from child process function f')
#     print('hello',name)
#
# if __name__ == '__main__':
#     info('main process line')
#     p = Process(target=f,args=('bob',))
#     p.start()
#     p.join()


from multiprocessing import Process
import time
import os

def task():


    print("%s is running,parent id is <%s>" % (os.getpid(), os.getppid()))
    time.sleep(3)
    print("%s is done,parent id is <%s>" % (os.getpid(), os.getppid()))


if __name__ == "__main__":

    t = Process(target=task, )
    t.start()

    print("主", os.getpid(), os.getppid())