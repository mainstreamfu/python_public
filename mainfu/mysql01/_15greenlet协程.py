from greenlet import greenlet
#greenlet遇到IO会并发，本质上上利用IO等待的时间，做其他事情
#grennlet遇到非IO会来回切换，耗时

# def test1():
#     print (11)
#     gr2.switch()
#     print (22)
#     gr2.switch()
#
# def test2():
#     print (33)
#     gr1.switch()
#     print (44)
#
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
# gr1.switch()

#

#
from gevent import monkey; monkey.patch_all()
import gevent
import time

def foo():
    print('11')
    time.sleep(3)
    print('22')

def bar():
    print('33')
    print('44')

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])