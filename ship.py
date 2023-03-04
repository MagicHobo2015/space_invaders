import pygame as pg
from character import Character
from colors import RED
from vector import Vector
from sound import Sound
from pygame.sprite import Sprite


class Ship(Character):
    def __init__(self, game, color=RED, rect=None, v=Vector(), image=None):
        super().__init__(color=color, rect=rect, v=v, game=game, image=None)
        self.color = color
        self.v = v
        self.game = game
        self.settings = game.settings
        self.lasers = None            # to prevent circular definition; set later in set_lasers()
        self.screen = game.screen
        self.image = pg.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.firing = False

    def set_lasers(self, lasers):
        self.lasers = lasers

    def fire(self):
        # print('ship is firing!')
        self.lasers.add()
        print(len(self.lasers.lasers))

    def open_fire(self):
        self.firing = True


    def cease_fire(self): self.firing = False

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)

    def update(self):
        super().update()
        if self.firing: self.fire()

    def draw(self):
        self.screen.blit(self.image, self.rect)
