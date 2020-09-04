import socket
from pickle import dumps, loads

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.36"
        self.port = 8820
        self.addr = (self.server, self.port)
        self.player = None
        self.connect()

    def set_player(self, p):
        self.player = p
    
    def get_player(self):
        return self.player
    
    def get_client(self):
        return self.client
    
    def connect(self):
        try:
            self.client.connect(self.addr)
        except:
            pass
    
    def send(self, data):
        try:
            self.client.send(dumps(data))
            return loads(self.client.recv(4096*4))
        except socket.error as e:
            print(e)

