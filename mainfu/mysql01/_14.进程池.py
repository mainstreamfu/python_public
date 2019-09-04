from multiprocessing import Pool,Process
import time

def Foo(i):
    time.sleep(1)
    return i + 100
def Bar(arg):
    print('number::',arg)

# if __name__=='__main__':
#     pool = Pool(3)
#     for i in range(10):
#         # pool.apply_async(func=Foo,args=(i,),callback=Bar)
#         # pool.apply(func=Foo, args=(i,))
#         pool.apply_async(func=Foo,args=(i,),callback=Bar)
#         pool.close()
#         pool.join()

if __name__ == "__main__":
    pool = Pool(3)#定义一个进程池，里面有3个进程
    for i in range(10):
        pool.apply_async(func=Foo, args=(i,),callback=Bar)
        #pool.apply(func=Foo, args=(i,))

    pool.close()#关闭进程池
    pool.join()#进程池中进程执行完毕后再关闭,(必须先close在join)

