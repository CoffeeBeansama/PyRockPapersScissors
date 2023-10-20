import pygame as pg

class Game:
    def __init__(self,id):

        self.playerOneFinished = False
        self.playerTwoFinished = False
        self.id = id
        self.objects = [None,None]
        self.turn = -1
    
    def getPlayerObject(self,turn,object):
        if turn == 0:
            self.objects[0] = object
        elif turn == 1:
            self.objects[1] = object

    
        self.evaluate()

    def evaluate(self):
        
        if self.objects[0] and self.objects[1] is not None:
            print(self.objects)
            print("Winner")
        else:
            pass




    


    



