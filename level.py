import pygame as pg
from network import Network
from support import *
from timer import Timer

class Level:
    def __init__(self):
        self.netWork = Network()
        self.player1Data = self.netWork.getPlayer()
        self.screen = pg.display.get_surface()

        self.spriteSize = (120,120)
        self.sprites = {
            "Rock": loadSprite("Sprites/rock.png",self.spriteSize),
            "Paper": loadSprite("Sprites/paper.png", self.spriteSize),
            "Scissor": loadSprite("Sprites/scissor.png", self.spriteSize),
        }

        self.turn = 1
        self.rock = self.screen.blit(self.sprites["Rock"].convert_alpha(), (200, 180))
        self.paper = self.screen.blit(self.sprites["Paper"].convert_alpha(), (340, 180))
        self.scissors = self.screen.blit(self.sprites["Scissor"].convert_alpha(), (480, 180))

        self.turnFinished = False

        self.timer = Timer(300,self.resetTurn)

    def handleUiEvent(self):
        mousePos = pg.mouse.get_pos()
        mousePressed = pg.mouse.get_pressed()

        self.rock = self.screen.blit(self.sprites["Rock"].convert_alpha(), (200, 180))
        self.paper = self.screen.blit(self.sprites["Paper"].convert_alpha(), (340, 180))
        self.scissors = self.screen.blit(self.sprites["Scissor"].convert_alpha(), (480, 180))

        self.getUiPressed(self.rock,mousePos,mousePressed)
        self.getUiPressed(self.paper,mousePos,mousePressed)
        self.getUiPressed(self.scissors,mousePos,mousePressed)

    def resetTurn(self):
        if self.turnFinished:
            self.turnFinished = False

    def getUiPressed(self,ui,mousePos,mousePressed):
        if not self.timer.activated:
            if ui.collidepoint(mousePos) and not self.turnFinished:
                if mousePressed[0]:
                    self.turn += 1
                    if self.turn >= 3:
                        self.turn = 1
                    self.turnFinished = True
                    self.timer.activate()



    def update(self):
        self.timer.update()
        self.player2Data = self.netWork.send(self.player1Data)
        self.handleUiEvent()


