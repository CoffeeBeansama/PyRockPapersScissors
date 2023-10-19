import pygame as pg

class Player:
    def __init__(self,id,name,object=None):
        self.id = id
        self.object = object
        self.name = name


    def setObject(self,object):
        self.object = object

    def reset(self):
        self.object = None

    def update(self,turn):
        print(self.name)

