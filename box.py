import pygame as pg
from vector import Vector
from random import randint
from sound import Sound
from util import Util
from character import Characters, Character


class Boxes(Characters):
    n_boxes = 0
        
    def __init__(self, initial_elements, width, height, game, color=None, random_sizes=True, image=None):
        super().__init__(initial_elements=initial_elements, width=width, height=height, game=game, color=color, random_sizes=random_sizes, image=image)
        # print(f'In Characters constructor...')

    def add(self, width, height, game, color=None, random_sizes=True, image=None):   
            w, h = width, height if not random_sizes else Util.random_sizes(game, 5, game.window_width / 5.0, 5, game.window_height / 5.0)
            max_v = game.max_v
            rect, v = Util.random_posn_velocity(game=game, width=width, height=height)     
            if color is None: color = Util.random_color()
            self.elements.append(Box(color=color, v=v, rect=rect, game=game, image=image))
            Boxes.n_boxes += 1

    def update(self):
        super().update()
        for el in self.elements:
            if self.game.player.rect.colliderect(el):
                self.elements.remove(el)
                self.game.sound.play_pickup()
        self.draw()
    
    
class Box(Character):
    def __init__(self, color, rect, v, game, image=None):
        super().__init__(color=color, rect=rect, v=v, game=game, image=image)
        # print(f'In Box constructor...')

    def __str__(self):
        return f'Box(clr={self.color},r={self.rect},v={self.v})'

    # def update(self): pass     # inherited from super class
    
    def draw(self):
        screen = self.screen
        r = self.rect
        img = self.image
        pg.draw.rect(screen, self.color, r) if img is None else screen.blit(img, r)
