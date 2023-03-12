import pygame as pg
from pygame.sprite import Sprite
from timer import Timer
import random
import time


class Mothership(Sprite):
    
    mother_ship_axplosions = [pg.transform.rotozoom(pg.image.load("images/explosion_100.png"), 0, 3),
                              pg.transform.rotozoom(pg.image.load("images/explosion_200.png"), 0, 3),
                              pg.transform.rotozoom(pg.image.load("images/explosion_300.png"), 0, 3)]
    
    
    def __init__(self, game):
        super().__init__()
        self.screen =game.screen
        self.game = game
        self.image = pg.transform.rotozoom(pg.image.load('images/motherShip.png'), 0, 2.0)
        self.rect = self.image.get_rect()
        self.rect.y = self.rect.height
        self.speed = game.settings.alien_speed
        self.score_board = game.scoreboard
        # this is so it always runs through a timer then when i want an explosion i just change it
        self.normal_timer = Timer([self.image], delay=300)
        self.timer = self.normal_timer
        self.explosion_timer = Timer(Mothership.mother_ship_axplosions, delay=300, is_loop=False)
        # this just gets a random number and if its even she goes left if its odd she goes right
        self.direction = 1 if random.randint(0, 100) % 2 == 0 else -1
        # this sets the x pos, if direction is left it starts at 0.0, if its going right it starts at 1200
        self.x = float(self.rect.x) if self.direction > 0 else float(self.screen.get_width()- 1)
        # this is just a flag for mother
        self.mother_out = False
        self.random_number = random.randint(1, 100)
        self.dying = False
        # self.explosion_timer = 
        
    
    # this will return true off your of screen
    def check_edges(self): 
       if self.x > 1200 or self.x < 0:
           self.mother_out = False
           self.x = float(self.rect.x) if self.direction > 0 else float(self.screen.get_width()- 1)
    
    # if it gets hit this will increment score and start explosion animation,
    # TODO: make this 
    def hit(self):
        if not self.dying:
            self.dying = True
            self.timer = self.explosion_timer
            self.game.scoreboard.increment_score()
            self.game.scoreboard.check_high_score()
            self.mother_out = False

    def check_collisions(self):
        collisions = pg.sprite.spritecollideany(self, self.game.ship_lasers.lasers)
        if collisions:
            self.hit()
    
    # this is where all the magic happens
    def update(self):
        if self.timer == self.explosion_timer and self.timer.is_expired():
            self.kill()
        # if shes out then move her
        if self.mother_out:
            self.check_collisions()
            self.x += (self.speed * self.direction)
            self.rect.x = self.x
            self.draw()
        else:
            #check to see if she should be
            ticks = time.time()
            if int(ticks) % self.random_number == 0:
                self.mother_out = True
        self.check_edges()    
        
    def reset_mother(self):
        self.mother_out = False
        self.random_number = self.random_number = random.randint(1, 100)
        self.x = float(self.rect.x) if self.direction > 0 else float(self.screen.get_width()- 1)
        
    # draws the image from the timer
    def draw(self):
        image = self.timer.image()
        rect = image.get_rect()
        rect.centerx, rect.centery = self.rect.centerx, self.rect.centery
        self.screen.blit(image, rect)