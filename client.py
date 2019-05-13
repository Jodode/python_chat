import socket
import select 
import sys 

class Client(object):
    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        
    def connect(self, dest_ip, dest_port=31337):
        self.conn = socket.socket()
        self.dest_host_port = (dest_ip, dest_port)
        self.conn.connect(self.dest_host_port)

    def start_chat(self):
        while 1:
            sockets_list = [sys.stdin, self.conn]
            read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 

            for socks in read_sockets:
                if socks == self.conn:
                    msg = socks.recv(2048)
                    print(msg.decode())
                else:
                    msg = sys.stdin.readline()
                    self.conn.send(msg.encode())
                    print("<You>", msg)

user = Client()
user.connect("127.0.0.1")   
user.start_chat()