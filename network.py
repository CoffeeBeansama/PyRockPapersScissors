import socket
import pickle
from settings import server

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.hostname = socket.gethostname()
        self.server = server
        self.port = 5559
        self.addr = (self.server,self.port)
        self.player = self.connect()

    def getPlayer(self):
        return self.player
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(4068*2).decode()
        except:
            pass

    def send(self,data):
        try:
            self.client.send(str.encode(data))  
            return pickle.loads(self.client.recv(4068*2))
        except socket.error as e:
            pass

