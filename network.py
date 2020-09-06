import socket
from pickle import dumps, loads
import struct

class Network:
    LENGTH = 4096
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.33"
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
            print(f"[CLIENT] Sending {data} which is {dumps(data)}")
            self.client.send(dumps(data))
            buf = b''
            while len(buf) < 4:
                buf += self.client.recv(4 - len(buf))
            length = struct.unpack('!I', buf)[0]
<<<<<<< HEAD
            sent = self.client.recv(length)
            sent = loads(sent)
=======
            print("[CLIENT] Length of packet sent back is: ", length)
            sent = self.client.recv(length)
            sent = loads(sent)
            print("[CLIENT] Message recieved: ", sent)
>>>>>>> 1b7bc4129fcf58a8cb31c2527e07944538960e61
            return sent
        except socket.error as e:
            print(e)

