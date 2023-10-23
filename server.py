import socket
from _thread import *
import pickle
from gameData import Game
from settings import playerObjects


class Server:
    def __init__(self):
        self.hostname = socket.gethostname()
        self.server = "192.168.1.10"

        self.port = 5559

        self._socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        self.gameIdCount = 0

        self.games = {}
        self.idCount = 0

        self.startServer()

        self.currentPlayers = 0

    def startServer(self):
        try:
            self._socket.bind((self.server,self.port))
        except socket.error as e:
            pass

        self._socket.listen()
        print("Waiting for connection...Server started!")

    def threadedClient(self,conn,player,gameId):
        conn.send(str.encode(str(player)))

        reply = ""
        while True:
            try:
                data = conn.recv(4068).decode()
                if gameId in self.games:
                    game = self.games[gameId]
                    if not data:
                        break
                    else:
                       
                        if data != "get":
                            if data in playerObjects:
                                game.getPlayerObject(player,data)

                            elif data == "p1":
                                game.increasePlayer1Score()

                            elif data == "p2":
                                game.increasePlayer2Score()

                            elif data == "reset":
                                game.resetObjects()
                                
                            else:
                                game.updateScores(player,data)
                                                   
                        conn.sendall(pickle.dumps(game))
                else:
                    break
            except:
                
                break
        
        print("Lost connection")

        try:
            del self.games[gameId]
        except:
            
            pass
        self.idCount -= 1
        conn.close()
        
        print("Connection lost")
        conn.close()

    def run(self):
        while True:
            conn,addr = self._socket.accept()

            self.idCount += 1
            player = 0
            gameId = (self.idCount -1) // 2

            if self.idCount % 2 == 1:
                self.games[gameId] = Game(gameId)
            else:
                player = 1

            
            start_new_thread(self.threadedClient,(conn,player,gameId))
           




server = Server()
server.run()


