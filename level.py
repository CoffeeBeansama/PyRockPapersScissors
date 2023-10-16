import pygame as pg
from network import Network

class Level:
    def __init__(self):
        self.netWork = Network()
        self.player1Data = self.netWork.getPlayer()

    def update(self):
        self.player2Data = self.netWork.send(self.player1Data)