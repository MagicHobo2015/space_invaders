import pygame as pg
from pygame.sprite import Sprite
from laser import Lasers
from vector import Vector
from sys import exit
from timer import  Timer
from utils import Util

class Ship(Sprite):  # TODO -- change to use YOUR OWN IMAGE for the ship AND its explosion

    ship_images = [pg.transform.rotozoom(pg.image.load(f'images/ship.png'), 0, 3)]
    # ship_hit_images = [pg.transform.rotozoom(pg.image.load(f'images/ship_fields{n}.png'), 0, 1.0) for n in range(9)]
    ship_explosion_images = [pg.transform.rotozoom(pg.image.load(f'images/ship_explode{n}.png'), 0, 3.0) for n in range(6)]

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.sound = game.sound
        self.ships_left = game.settings.ship_limit  

        self.image = pg.transform.rotozoom(pg.image.load('images/ship.png'), 0, 3)
        self.ship_life_image = pg.image.load('images/ship.png')
        
        self.rect = self.image.get_rect()
        self.screen_rect = game.screen.get_rect()
        self.posn = self.center_ship()    # posn is the centerx, bottom of the rect, not left, top
        self.v = Vector()

        # self.lasers = Lasers(settings=self.settings)
        self.lasers = game.ship_lasers

        # self.lasers = lasers
        self.firing = False
        self.lasers_attempted = 0

        self.timer_normal = Timer(image_list=Ship.ship_images)
        self.timer_explosion = Timer(image_list=Ship.ship_explosion_images, delay=200, is_loop=False)  
        self.timer = self.timer_normal    
        self.dying = self.dead = False
        self.stats = game.stats
        self.sb = game.scoreboard


    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        return Vector(self.rect.left, self.rect.top)
    
    def fire(self):
        if len(self.lasers.lasers) < self.settings.lasers_allowed:
            self.lasers.add()

    def open_fire(self): self.firing = True
    def cease_fire(self): self.firing = False

    def reset(self): 
        self.v = Vector()
        self.posn = self.center_ship()
        self.dying = self.dead = False
        self.lasers.reset()             # these are called ship_lasers in game
        self.timer = self.timer_normal
        self.timer_explosion.reset()
        self.rect.left, self.rect.top = self.posn.x, self.posn.y

    def hit(self):
        if not self.dying:
            print('SHIP IS HIT !!!!!!!!!!!!!!!!!!!!!')
            self.dying = True 
            self.timer = self.timer_explosion

    def really_dead(self):
        self.ships_left -= 1
        self.draw_ship_lives()
        print(f'Ship is dead! Only {self.ships_left} ships left')
        self.game.death_reset() if self.ships_left > 0 else self.game.game_over()

    def update(self):
        if self.timer == self.timer_explosion and self.timer.is_expired():
            print('ship timer has expired it is now really dead ......')
            self.really_dead()
        self.posn += self.v
        self.posn, self.rect = Util.clamp(posn=self.posn, rect=self.rect, settings=self.settings)
        if self.firing:
            self.lasers_attempted += 1
            if self.lasers_attempted % self.settings.lasers_every == 0:
                self.lasers.shoot(game=self.game, x = self.rect.centerx, y=self.rect.top)
        self.lasers.update()
        self.draw()

    def draw(self): 
        image = self.timer.image()
        rect = image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        rect.top -= 50                                        # MODIFICATION for SHIP's SHIELDS
        self.screen.blit(image, rect)
        # self.screen.blit(self.image, self.rect)

    def draw_ship_lives(self):
        x = 10
        y = self.screen_rect.bottom - 50
        for i in range(self.ships_left - 1):
            if i < self.stats.ships_left:
                self.screen.blit(self.ship_life_image, (x + i * 50, y))
