import pygame as pg
from network import Network
from support import *
from timer import Timer


class Level:
    def __init__(self):
        pg.font.init()
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

        self.font = pg.font.Font("font/DeterminationMonoWebRegular-Z5oq.ttf",32)
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
                        self.addScore(self.player1Data)
                    else:
                        self.addScore(self.player2Data)
                elif player1 == "Paper":
                    if player2 == "Rock":
                        self.addScore(self.player1Data)
                    else:
                        self.addScore(self.player2Data)
                elif player1 == "Scissor":
                    if player2 == "Paper":
                        self.addScore(self.player1Data)
                    else:
                        self.addScore(self.player2Data)

                self.player2Data.reset()
                self.player1Data.reset()

    def addScore(self,player):
        player.score += 1
        print(f"winner: {player.name}")

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


    def handleUiTexts(self):
        if self.player1Data.id == 0:
            score1Pos = (30, 400)
            score2Pos = (580, 400)
        else:
            score1Pos = (30, 400)
            score2Pos = (580, 400)

        player1score = self.font.render(f"You: {str(self.player1Data.score)}",True,(255,255,255))
        player2score = self.font.render(f"Player 2: {str(self.player2Data.score)}",True,(255,255,255))
        notifText = self.font.render("Pick your weapon!" if not self.player1Data.object else "Waiting for player 2..",True,(255,255,255))

        notifTextPos = (270,100) if not self.player1Data.object else (240,100)
        self.screen.blit(notifText, notifTextPos)

        self.screen.blit(player1score, score1Pos)
        self.screen.blit(player2score, score2Pos)
        self.evaluateWinner()

    def update(self):
        self.timer.update()
        self.player2Data = self.netWork.send(self.player1Data)

        self.handleUiTexts()

        self.handleUiEvent()


