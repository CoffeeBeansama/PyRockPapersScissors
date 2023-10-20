import socket
from _thread import *
import pickle
from player import Player

class Server:
    def __init__(self):
        self.hostname = socket.gethostname()
        self.server = socket.gethostbyname(self.hostname)

        self.port = 5558

        self._socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        self.players = [Player(0,"Player 1"), Player(1,"Player 2")]

        self.gameIdCount = 0

        self.startServer()

        self.currentPlayers = 0

    def startServer(self):
        try:
            self._socket.bind((self.server,self.port))
        except socket.error as e:
            print(e)

        self._socket.listen()
        print("Waiting for connection...Server started!")


    def threadedClient(self,conn,player):
        conn.send(pickle.dumps(self.players[player]))
        reply = ""
        while True:
            try:
                data = pickle.loads(conn.recv(2048))
                self.players[player] = data
                if not data:
                    break
                else:
                    if player == 1:
                        reply = self.players[0]
                    else:
                        reply = self.players[1]

                conn.sendall(pickle.dumps(reply))
            except:
                break
        print("Connection lost")
        conn.close()

    def run(self):
        while True:
            conn,addr = self._socket.accept()
            start_new_thread(self.threadedClient,(conn,self.currentPlayers))
            self.currentPlayers += 1
            if self.currentPlayers >= 3:
                self.currentPlayers -= 1




server = Server()
server.run()


