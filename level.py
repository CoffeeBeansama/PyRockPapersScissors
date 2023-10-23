import pygame as pg
from network import Network
from support import *
from timer import Timer


class Level:
    def __init__(self):
        pg.font.init()
        self.netWork = Network()
        try:
            self.playerID = int(self.netWork.getPlayer())
        except:
            pass
        self.screen = pg.display.get_surface()
        self.spriteSize = (120,120)
        self.sprites = {
            "Rock": loadSprite("Sprites/rock.png",self.spriteSize),
            "Paper": loadSprite("Sprites/paper.png", self.spriteSize),
            "Scissor": loadSprite("Sprites/scissor.png", self.spriteSize),
        }

        self.rock = self.screen.blit(self.sprites["Rock"].convert_alpha(), (200, 180))
        self.paper = self.screen.blit(self.sprites["Paper"].convert_alpha(), (340, 180))
        self.scissors = self.screen.blit(self.sprites["Scissor"].convert_alpha(), (480, 180))

        self.font = pg.font.Font("font/DeterminationMonoWebRegular-Z5oq.ttf",32)

        
        self.buttonClicked = False
        self.timer = Timer(500,self.resetTurn)

        self.playerScore = 0

        self.playerPicked = False


    def handleUiEvent(self):
        mousePos = pg.mouse.get_pos()
        mousePressed = pg.mouse.get_pressed()

        self.rock = self.screen.blit(self.sprites["Rock"].convert_alpha(), (200, 180))
        self.paper = self.screen.blit(self.sprites["Paper"].convert_alpha(), (340, 180))
        self.scissors = self.screen.blit(self.sprites["Scissor"].convert_alpha(), (480, 180))

        self.getUiPressed(self.rock,mousePos,mousePressed,"Rock")
        self.getUiPressed(self.paper,mousePos,mousePressed,"Paper")
        self.getUiPressed(self.scissors,mousePos,mousePressed,"Scissor")

    def evaluateWinner(self):
        pass

    def addScore(self,player):
        pass

    def resetTurn(self):
        if self.buttonClicked:
            self.buttonClicked = False

    def getUiPressed(self,ui,mousePos,mousePressed,getObject):
        if not self.timer.activated:
            if ui.collidepoint(mousePos) and not self.buttonClicked:
                if mousePressed[0]:
                    self.playerPicked = True
                    
                    if self.game.haventPicked(self.playerID):
                        self.game = self.netWork.send(getObject)
                    
                    if self.game.bothPlayersPicked():
                        if self.game.evaluate() == self.playerID:
                            self.netWork.send("p1")
                        else:
                            self.netWork.send("p2")
                
                        self.netWork.send("reset")
                        
                    self.buttonClicked = True
                    self.timer.activate()



    def handleUiTexts(self,player1Score,player2Score):
        score1Pos = (30, 400)
        score2Pos = (580, 400)

        try:
            player1score = self.font.render(f"You: {player1Score}",True,(255,255,255))
            player2score = self.font.render(f"Player 2: {player2Score}",True,(255,255,255))

            

            text = "Pick your weapon!" if self.game.haventPicked(self.playerID) else "Waiting for player 2.."
            notifText = self.font.render(text,True,(255,255,255))

            notifTextPos = (270,100)
            self.screen.blit(notifText, notifTextPos)

            self.screen.blit(player1score, score1Pos)
            self.screen.blit(player2score, score2Pos)
        except:
            pass

    def update(self):
        self.timer.update()
        self.game = self.netWork.send("get")

        


        self.handleUiEvent()
        self.handleUiTexts(self.game.getP1Score(self.playerID),self.game.getP2Score(self.playerID))
            
          

        
        


