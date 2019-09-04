# import socket
#
# ip_port = ('127.0.0.1',8080)
#
# sk = socket.socket()
# sk.bind(ip_port)
# sk.listen(5)
# flag = True
#
# while flag:
#     conn,addr = sk.accept()
#     client_data = conn.recv(1024).decode()
#     print(client_data)
#     conn.sendall('test'.encode())
#     conn.close()

# from socket import *
#
# from time import ctime
#
# HOST = ''
# PORT = 8080
# BUFSIZ = 1024
# ADDR = (HOST,PORT)
#
# tcpSerSock = socket(AF_INET,SOCK_STREAM)
# tcpSerSock.bind(ADDR)
# tcpSerSock.listen(5)#listen的参数指的是服务器在拒绝新链接前最多接受的未连接数
#
#
# while True:
#     print('waiting for connecting...')
#     tcpCliSock,addr = tcpSerSock.accept()
#     print('...connecting from :',addr)
#
#     while True:
#         data = tcpCliSock.recv(BUFSIZ)
#         if not data:
#             break
#         data = '[{}] {}'.format(ctime(),data.decode('utf-8'))
#         print(data)
#         tcpCliSock.send(data.encode('utf-8'))
#     tcpCliSock.close()
#
# tcpSerSock.close()

from socket import *
from time import ctime
from select import select

HOST = ''
POST = 8080
BUFSIZ = 1024
ADDR = (HOST, POST)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

tcpSerSock.setblocking(False)  # 将tcpSerSock设置为非租塞模式
inputs = [tcpSerSock]

print('waiting for connnecting...')

while True:
    rlist, wlist, xlist = select(inputs, [], [])

    for s in rlist:
        if s is tcpSerSock:
            tcpCliSock, addr = s.accept()
            print('...connecting from:', addr)

            tcpCliSock.setblocking(False)  # 将tcpCliSock设置为非租塞模式
            inputs.append(tcpCliSock)      # 将tcpCliSock插入inputs中

        else:
            data = s.recv(BUFSIZ)

            if not data:
                inputs.remove(s)
                s.close()
                continue

            data = '[{}] {}'.format(ctime(), data.decode('utf-8'))
            s.send(data.encode('utf-8'))