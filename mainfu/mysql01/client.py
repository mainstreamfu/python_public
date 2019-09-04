# import socket
#
# ip_port = ('127.0.0.1',8080)
#
# sk = socket.socket()
#
# sk.connect(ip_port)
#
# sk.sendall('来了'.encode())
#
# server_replay = sk.recv(1024).decode()
# print(server_replay)
#
# sk.close()


from socket import *

HOST = 'localhost'
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('>')
    if not data:
        break
    tcpCliSock.send(data.encode('utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

tcpCliSock.close()