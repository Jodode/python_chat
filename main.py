import socket

class Server(object):
    """Uturu + Jodode = best chat"""

    def __init__(self, max_connections=5, host="", port=31337):
        self.max_connections = max_connections
        self.host = host
        self.port = port

    def open_server(self):
        self.sock = socket.socket()
        self.sock.bind((self.host, self.port))
        self.sock.listen(self.max_connections)

    def run_server(self):
        while 1:
            conn, addr = self.sock.accept()
            data = self.conn.recv(16384)
            udata = data.decode("utf-8")
            print("Data: " + udata)

#
def get_ip():
    return socket.gethostbyname(socket.gethostname())



first_server = Server()
first_server.open_server()
first_server.run_server()

# print("Share your ip with your friends\nYour IP:", get_ip(), end="\n\n")
# pass
#
# host = input("Enter your friend's ip:\n > ")
host_port = (get_ip(), 31337)
#
# print("IP: " + host_port[0] + "\nport: " + str(host_port[-1]))

conn = socket.socket()
conn.connect(host_port)

conn.send(b'Kek\n')

# print("Data: " + udata)

