import pygame as pg
from level import Level

class Game:
    def __init__(self):
        self.window = pg.display.set_mode((800,500))
        self.clock = pg.time.Clock()
        pg.display.set_caption("PyMortalKombat")
        self.running = True
        self.level = Level()



    def run(self):
        while self.running:

            self.clock.tick(60)
            pg.display.set_caption(f"player: {self.level.player1Data.name}")
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    pg.quit()


            self.window.fill("black")
            self.level.update()
            pg.display.update()




game = Game()
game.run()