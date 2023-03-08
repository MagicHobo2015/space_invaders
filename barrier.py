import pygame as pg
from pygame.sprite import Sprite, Group

class Barrier(Sprite):    # not a real Barrier class -- should be made up of many tiny Sprites
                          # you will not get credit for this class unless it is updated to tiny Sprites
    color = 255, 0, 0
    black = 0, 0, 0

    def __init__(self, game, rect):
        super().__init__()
        self.screen = game.screen
        self.rect = rect
        self.settings = game.settings
        
    def hit(self): # TODO: change to use tiny Sprites
        pass

    def update(self): 
        # TODO: change to use tiny Sprites to decide if a collision occurred
        self.draw()

    def draw(self): 
        # TODO: change to use tiny Sprites
        pg.draw.rect(self.screen, Barrier.color, self.rect, 0, 20)
        pg.draw.circle(self.screen, self.settings.bg_color, (self.rect.centerx, self.rect.bottom), self.rect.width/6)


class Barriers:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.create_barriers()

    def create_barriers(self):     
        width = self.settings.screen_width / 10
        height = 2.0 * width / 4.0
        top = self.settings.screen_height - 2.1 * height
        rects = [pg.Rect(x * 2 * width + 1.5 * width, top, width, height) for x in range(4)]   # SP w  3w  5w  7w  SP
        self.barriers = [Barrier(game=self.game, rect=rects[i]) for i in range(4)]

    def hit(self): pass 
    
    def reset(self):
        self.create_barriers()

    def update(self):
        for barrier in self.barriers: 
            barrier.update()

    def draw(self):
        for barrier in self.barriers: 
            barrier.draw()

