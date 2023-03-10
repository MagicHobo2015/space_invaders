import pygame as pg
from pygame.sprite import Sprite, Group
from timer import Timer

class Barrier(Sprite):    # not a real Barrier class -- should be made up of many tiny Sprites
                          # you will not get credit for this class unless it is updated to tiny Sprites
    color = 255, 0, 0
    black = 0, 0, 0
    barrier_images = [pg.transform.rotozoom(pg.image.load("images/shield-5.png"), 0, 4),
                      pg.transform.rotozoom(pg.image.load("images/shield-4.png"), 0, 4),
                      pg.transform.rotozoom(pg.image.load("images/shield-3.png"), 0, 4),
                      pg.transform.rotozoom(pg.image.load("images/shield-2.png"), 0, 4),
                      pg.transform.rotozoom(pg.image.load("images/shield-1.png"), 0, 4)]

    barrier_explosions = [pg.image.load(f'images/explosions/shield_explosion_{num}.png') for num in range(1,3)]

    def __init__(self, game, rect):
        super().__init__()
        self.screen = game.screen
        self.rect = rect
        self.settings = game.settings
        self.barrier_life = 5
        self.game = game
        self.dying = False
        self.timer_explosion = Timer(self.barrier_explosions, delay=300, is_loop=False)
        
        
    def hit(self): # TODO: change to use tiny Sprites
        if self.barrier_life < 0:
            self.dying = True
        else:
            self.barrier_life -= 1

    def update(self): 
        # TODO: change to use tiny Sprites to decide if a collision occurred
        if pg.sprite.spritecollide(self, self.game.aliens.aliens_lasers.lasers, True):
            self.hit()
        self.draw()

    def draw(self):
        if not self.dying:
            self.screen.blit(self.barrier_images[self.barrier_life-1], self.rect)
        elif self.dying:
            image = self.timer_explosion.image()
            self.screen.blit(image, self.rect)

class Barriers:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.create_barriers()

    def create_barriers(self):     
        width = self.settings.screen_width / 10
        height = 2.0 * width / 4.0
        top = self.settings.screen_height - 4 * height
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

