from threading import Thread
from tkinter import *

class ReceiveThread(Thread):
    def __init__(self,tcpCliSock,BUFSIZ=1024):
        Thread.__init__(self)
        self.daemon = True
        self.tcpCliSock = tcpCliSock
        self.BUFSIZ = BUFSIZ


    def run(self):
        while True:
            data = self.tcpCliSock.recv(self.BUFSIZ)
            if not data:
                self.tcpCliSock.close()
                root.destroy()

            else:
                Output.insert(END, data.decode('utf-8'))