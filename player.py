import pygame as pg

class Player:
    def __init__(self,id,name,object=None):
        self.id = id
        self.object = object
        self.name = name

    def setObject(self,object):
        self.object = object
        print(f"{self.name}: {self.object}")


    def update(self,turn):
        print(self.name)

