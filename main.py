import socket
from multiprocessing import Process

class Client(object):

    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname())

    def connect(self, dest_ip, dest_port=31337):
        self.conn = socket.socket()
        self.dest_host_port = (dest_ip, dest_port)
        self.conn.connect(self.dest_host_port)

    def send_message(self, msg):
        print("LOL")
        self.conn.send(msg.encode() + b'\n')

    def get_response(self):
        print(self.conn.recv(1024))

# class Server(object):
#     """Uturu + Jodode = best chat"""

#     def __init__(self, max_connections=5, host="", port=31337):
#         self.max_connections = max_connections
#         self.host = host
#         self.port = port

#     def open_server(self):
#         self.sock = socket.socket()
#         self.sock.bind((self.host, self.port))
#         self.sock.listen(self.max_connections)

#     def run_server(self):
#         while 1:
#             print("KEK")
#             conn, addr = self.sock.accept()
#             data = conn.recv(16384)
#             udata = data.decode("utf-8")
#             print("Data: " + udata)


first_server = Server()
first_server.open_server()

user = Client()
user.connect(user.ip)
t1 = Process(target=first_server.run_server)
t2 = Process(target=user.send_message, args=("lolkek",))
t3 = Process(target=user.get_response)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
# while 1:

#     t2.join()
#     t1.join()
# print("Share your ip with your friends\nYour IP:", get_ip(), end="\n\n")
# pass
#
# host = input("Enter your friend's ip:\n > ")
# host_port = (get_ip(), 31337)
#
# print("IP: " + host_port[0] + "\nport: " + str(host_port[-1]))

# conn = socket.socket()
# conn.connect(host_port)

# conn.send(b'Kek\n')

# print("Data: " + udata)

