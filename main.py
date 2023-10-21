import pygame as pg
from level import Level

class Main:
    def __init__(self):
        self.window = pg.display.set_mode((800,500))
        self.clock = pg.time.Clock()
        
        self.running = True

        self.level = Level()
        try:
            pg.display.set_caption(f"Player: {self.level.playerID+1}")
        except:
            pg.display.set_caption("Player not connected")


    def run(self):
        while self.running:
            self.clock.tick(60)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    pg.quit()


            self.window.fill("black")
            self.level.update()
            pg.display.update()




game = Main()
game.run()