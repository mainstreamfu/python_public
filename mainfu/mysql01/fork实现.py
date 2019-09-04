#创建简单的子进程

import os

pid = os.fork()

print(pid)

# if pid<0:
#     print('失败')
#
# elif pid ==0:
#     print('这是子进程')
#
# else:
#     print('这是一个父进程')
#

#注： 运行的次数不一致，会输出不同的结果。

#注：

#a）前后不一致， 原因：因为子进程和父进程是独立运行的。但最后是打印在同一个终端上，所以终端上父子进程会同时打印出。
#b）子进程运行时是从pid=os.fork()下面语句执行。该语句是两条语句：1、os.fork()是创建子进程语句；2、‘pid=’是赋值语句。所以在创建子进程后，下一句为运行赋值语句。
#c）在pid = os.fork()语句中，父进程先运行。运行过程中，子进程也在运行。但此刻并不代表父进程已经运行结束，所以会出现终端语句顺序混乱情况。
