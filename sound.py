import pygame as pg 
import time


class Sound:
    def __init__(self): 
        self.pickup = pg.mixer.Sound('sounds/pickup.wav')
        self.gameover = pg.mixer.Sound('sounds/gameover.wav')
        self.lasers = pg.mixer.Sound('sounds/laser.wav')
        self.alien_explo = pg.mixer.Sound('sounds/alien explosion.wav')
        self.ship_explo = pg.mixer.Sound('sounds/ship_explosion.wav')
        self.music_playing = False
        pg.mixer.music.load('sounds/ride_of_the_valkyries.mp3')
        pg.mixer.music.set_volume(0.05)
        self.lasers.set_volume(0.01)
        self.gameover.set_volume(0.05)
        self.alien_explo.set_volume(0.02)
        self.ship_explo.set_volume(0.02)
                                             
    def play_background(self): 
        pg.mixer.music.play(-1, 0.0)
        self.music_playing = True
        
    def play_pickup(self): 
        if self.music_playing: self.pickup.play()

    def play_laser(self):
        self.lasers.play()

    def play_alien_explo(self):
        self.alien_explo.play()

    def play_ship_explo(self):
        self.ship_explo.play()

    def play_gameover(self):
        if self.music_playing: 
            self.stop_background()
            self.gameover.play()
            time.sleep(3.0)       # sleep until game over sound has finished
        
    def toggle_background(self):
        if self.music_playing: 
            self.stop_background()
        else:
            self.play_background()
        self.music_playing = not self.music_playing
        
    def stop_background(self): 
        pg.mixer.music.stop()
        self.music_playing = False 
    
        
    
    
