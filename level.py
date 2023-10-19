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

        self.turn = 0
        self.rock = self.screen.blit(self.sprites["Rock"].convert_alpha(), (200, 180))
        self.paper = self.screen.blit(self.sprites["Paper"].convert_alpha(), (340, 180))
        self.scissors = self.screen.blit(self.sprites["Scissor"].convert_alpha(), (480, 180))

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
        self.player1Data.setObject(object)

    def evaluateWinner(self):
        player1 = self.player1Data.object
        player2 = self.player2Data.object

        if player2 and player1:
            draw = player1 == player2

            print(f"player 1: {player1}")
            print(f"player 2: {player2}")

            if draw:
                print("Its a draw!!")
                self.player1Data.reset()
                self.player2Data.reset()
            else:
                if player1 == "Rock":
                    if player2 == "Scissor":
                        print(f"Player {self.player1Data.id} win")
                    else:
                        print(f"Player {self.player2Data.id} win")
                elif player1 == "Paper":
                    if player2 == "Rock":
                        print(f"Player {self.player1Data.id} win")
                    else:
                        print(f"Player {self.player2Data.id} win")
                elif player1 == "Scissor":
                    if player2 == "Paper":
                        print(f"Player {self.player1Data.id} win")
                    else:
                        print(f"Player {self.player2Data.id} win")

                self.player2Data.reset()
                self.player1Data.reset()





    def resetTurn(self):
        if self.buttonClicked:
            self.buttonClicked = False

    def getUiPressed(self,ui,mousePos,mousePressed,getObject):
        if not self.timer.activated:
            if ui.collidepoint(mousePos) and not self.buttonClicked:
                if mousePressed[0]:
                    self.getObjectPressed(getObject)
                    if self.turn == self.player1Data.id:
                        self.turn += 1

                    if self.turn >= 2:
                        self.turn = 0

                    self.buttonClicked = True
                    self.player2Data.reset()
                    self.timer.activate()



    def update(self):
        self.timer.update()
        self.player2Data = self.netWork.send(self.player1Data)

        self.evaluateWinner()


        self.handleUiEvent()


