import socket
import time
from threading import *

class Server(object):
    def __init__(self, max_connections=100, host="127.0.0.1", port=31337, port_list=60606):
        self.max_connections = max_connections
        self.host = host
        self.port = port
        self.port_list = port_list
        self.list_of_clients = []

    def open_server(self):
        self.sock_read = socket.socket()
        self.sock_read.bind(("", self.port_list))
        self.sock_write = socket.socket()
        self.sock_write.connect((self.host, self.port))
        self.sock.listen(self.max_connections)

    

    def run_server(self):
        def remove_conn(conn, addr):
            if conn in self.list_of_clients:
                print(addr[0], "disconnected")
                self.list_of_clients.remove(conn)

        def broadcast(msg, conn, addr):
            for client in self.list_of_clients:
                if client != conn:
                    try:
                        client.send(msg.encode())
                    except:
                        client.close()
                        remove_conn(client, addr)

        def client_thread(conn, addr):
            conn.send(str("Welcome " + "<" + addr[0] + "> !").encode())
            while 1:
                try:
                    msg = conn.recv(2048)
                    if msg:
                        print("<" + addr[0] + ">", msg.decode()[:-1])
                        msg_to_send = "<" + addr[0] + "> " + msg
                        broadcast(msg_to_send, conn, addr)
                    else:
                        remove_conn(conn)
                except: 
                    continue
        print("Server is starting on port", self.port)
        while 1:
            conn, addr = self.sock.accept()
            
            self.list_of_clients.append(conn)

            print(addr[0], "connected")

            Thread(target=client_thread, args=(conn, addr)).start() 

server = Server()
server.open_server()
server.run_server()
