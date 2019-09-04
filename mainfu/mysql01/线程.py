import threading


def show(arg):
    print('thread' + str(arg))


for i in range(3):
    t = threading.Thread(target=show, args=(1,))  # 也可以使用继承方式使用多线程，重写run方法
    t.start()

print('main thread stop')


