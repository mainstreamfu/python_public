from gevent import monkey; monkey.patch_all()
import gevent,requests

def fctch_async(method,url,reg_kwargs):
    print(method,url,reg_kwargs)
    respone = requests.request(method=method,url=url,**reg_kwargs)
    print(respone.url,len(respone.content))

#发送请求

gevent.joinall([
    #joinall里都是存放协程
    gevent.spawn(fctch_async,method='get',url='http://www.cnblogs.com/',reg_kwargs={}),
    gevent.spawn(fctch_async,method='get',url='http://www.baidu.com/',reg_kwargs={}),
    gevent.spawn(fctch_async,method='get',url='http://www.sogo.com/',reg_kwargs={})
])



