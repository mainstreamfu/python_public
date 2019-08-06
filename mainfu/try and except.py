import sys

#当我们觉得一段代码可能会出错时，
# 就可以用try语句。如果这段代码出错，
# 则直接跳过后面的代码，转到except X语句块，
# except X是用来捕获错误类型X的。最后可加上finally语句，
# 如果有finally语句，则执行之。



def fn(a):
    try:
        print('try')
        r = 10 / a
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    finally:
        print('finally')
    print('end')

    return print(11)

fn(0)

def fn(a):
    try:
        print('try')
        r = 10 / a
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    except ValueError as e:
        print('except:', e)
    except :
        print('unknow except')
    else:
        print('no errors')
    finally:
        print('finally')
    print('end')
    return
