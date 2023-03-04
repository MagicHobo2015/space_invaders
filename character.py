import pygame as pg
from vector import Vector
from random import randint
from sound import Sound
from util import Util
from abc import ABC, abstractmethod


class Characters(ABC):
    def __init__(self, initial_elements, width, height, game, color=None, random_sizes=True, image=None):
        # print(f'In Characters constructor...')
        self.elements = []
        self.game = game 
        self.image = image 

        for i in range(initial_elements):
            self.add(game=game, width=width, height=height, color=color, random_sizes=random_sizes, image=image)
        
    @abstractmethod
    def add(self, width, height, game, color=None, random_sizes=True, image=None): pass
    
    # @abstractmethod
    # def add_random(self): pass             
    
    def update(self):
        for el in self.elements:
            el.update()

    def draw(self):
        for el in self.elements:
            el.draw()


class Character(ABC):
    def __init__(self, color, rect, v, game, image=None):
        # print(f'In Character constructor...')

        self.screen = game.screen
        self.color = color
        self.rect = rect
        self.v = v
        self.game = game
        self.image = image

    def __str__(self):
        return f'Character(clr={self.color},r={self.rect},v={self.v})'

    def update(self):
        self.rect.left += self.v.x
        self.rect.top += self.v.y

        if self.rect.top < 0 or self.rect.bottom > self.game.window_height:
            self.v.y *= -1
        if self.rect.left < 0 or self.rect.right > self.game.window_width:
            self.v.x *= -1
        self.draw()

    @abstractmethod
    def draw(self): pass        # must be defined by subclass    
