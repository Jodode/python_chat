import socket
import select 
import sys
from threading import *
import time

class Client(object):
    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        
    def connect(self, dest_ip, dest_port=31337):
        self.conn_write = socket.socket()
        self.conn_write.connect((dest_ip, dest_port))

    def start_listen(self, list_port=60606):
        self.sock = socket.socket()
        self.sock.bind(("", list_port))
        self.sock.listen(1)
        self.conn_read, self.addr_read = self.sock.accept()

    def print_msg(self):
        self.start_listen()
        while 1:
            print(self.conn_read.recv(2048).decode())

    def start_chat(self):
        while 1:
            # sockets_list = [self.conn_write]
            # print(sockets_list)
            # read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])
            # print(read_sockets, write_socket, error_socket)
            #
            # for socks in read_sockets:
            #     if socks == self.conn_write:
            msg = sys.stdin.readline()
            self.conn_write.send(msg.encode())
            print("<You>", msg)


user = Client()
user.connect("127.0.0.1")
Thread(target=user.start_chat).start()
Thread(target=user.print_msg).start()