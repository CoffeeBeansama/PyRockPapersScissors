import pygame as pg

class Game:
    def __init__(self,id):

        self.playerOneFinished = False
        self.playerTwoFinished = False
        self.id = id
        self.objects = [None,None]
        self.scores = [0,0]
        self.turn = -1
    
    def getPlayerObject(self,playerID,object):
        if playerID == 0:
            self.objects[0] = object
        elif playerID == 1:
            self.objects[1] = object

    def increasePlayer1Score(self):
        self.scores[0] += 1
    
    def increasePlayer2Score(self):
        self.scores[1] += 1


       
      

    def resetObjects(self):
        for i in range(len(self.objects)):
            self.objects[i] = None

 

    def playersPicked(self):
        p1 = self.objects[0]
        p2 = self.objects[1]
        if p1 and p2 is not None:
            return True
        return False

    def getP1Score(self,playerID):
        return self.scores[playerID]
    
    def getP2Score(self,playerID):
        match playerID:
            case 0:
                return self.scores[1]
            case 1:
                return self.scores[0]
    
    def evaluate(self):
        p1 = self.objects[0]
        p2 = self.objects[1]
        
        self.winner = -1

        if p1 == p2:
            print("its a draw!")
        elif p1 == "Rock":
            if p2 == "Scissor":
                self.winner = 0
            else:
                self.winner = 1
        elif p1 == "Paper":
            if p2 == "Rock":
                self.winner = 0
            else:
                self.winner = 1
        elif p1 == "Scissor":
            if p2 == "Paper":
                self.winner = 0
            else:
                self.winner = 1
            
        
        print(self.objects)
        return self.winner
    
        




    


    



