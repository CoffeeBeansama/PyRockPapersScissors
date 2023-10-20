import pygame as pg
from network import Network
from support import *
from timer import Timer


class Level:
    def __init__(self):
        pg.font.init()
        self.netWork = Network()
        self.player1Data = int(self.netWork.getPlayer())
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

        self.turn = 0
        self.buttonClicked = False
        self.timer = Timer(500,self.resetTurn)


    def handleUiEvent(self):
        mousePos = pg.mouse.get_pos()
        mousePressed = pg.mouse.get_pressed()

        self.rock = self.screen.blit(self.sprites["Rock"].convert_alpha(), (200, 180))
        self.paper = self.screen.blit(self.sprites["Paper"].convert_alpha(), (340, 180))
        self.scissors = self.screen.blit(self.sprites["Scissor"].convert_alpha(), (480, 180))

        self.getUiPressed(self.rock,mousePos,mousePressed,"Rock")
        self.getUiPressed(self.paper,mousePos,mousePressed,"Paper")
        self.getUiPressed(self.scissors,mousePos,mousePressed,"Scissor")

    def getObjectPressed(self,object):
        self.game.objects[self.turn] = object
        print(self.game.objects)
        
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
                    self.getObjectPressed(getObject)
                    self.turn += 1
                    if self.turn >= 2:
                        self.turn = 0
                    self.buttonClicked = True
                    self.timer.activate()


    def handleUiTexts(self):
        score1Pos = (30, 400)
        score2Pos = (580, 400)
        
        player1score = self.font.render(f"You: ",True,(255,255,255))
        player2score = self.font.render(f"Player 2: ",True,(255,255,255))
        notifText = self.font.render("Pick your weapon!",True,(255,255,255))

        notifTextPos = (270,100)
        self.screen.blit(notifText, notifTextPos)

        self.screen.blit(player1score, score1Pos)
        self.screen.blit(player2score, score2Pos)

    def update(self):
        self.timer.update()
        try:
            self.game = self.netWork.send("game")

            self.handleUiTexts()
     
            self.handleUiEvent()
        except:
            pass

        
        


