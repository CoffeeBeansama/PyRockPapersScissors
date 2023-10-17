import pygame as pg
from network import Network
from support import *

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

        self.rock = self.screen.blit(self.sprites["Rock"].convert_alpha(), (200, 180))
        self.paper = self.screen.blit(self.sprites["Paper"].convert_alpha(), (340, 180))
        self.scissors = self.screen.blit(self.sprites["Scissor"].convert_alpha(), (480, 180))

        self.ui = [self.rock,self.paper,self.scissors]

    def handleUiEvent(self):
        mousePos = pg.mouse.get_pos()
        mousePressed = pg.mouse.get_pressed()

        self.rock = self.screen.blit(self.sprites["Rock"].convert_alpha(), (200, 180))
        self.paper = self.screen.blit(self.sprites["Paper"].convert_alpha(), (340, 180))
        self.scissors = self.screen.blit(self.sprites["Scissor"].convert_alpha(), (480, 180))

        for ui in self.ui:
            if ui.collidepoint(mousePos):
                if mousePressed[0]:
                    print(ui)



    def update(self):
        self.player2Data = self.netWork.send(self.player1Data)
        self.handleUiEvent()


