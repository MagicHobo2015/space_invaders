import pygame as pg
from laser import LaserType
import time
import wave


class Sound:
    def __init__(self, bg_music):
        pg.mixer.init(frequency=88200)
        pg.mixer.music.load(bg_music)
        pg.mixer.music.set_volume(0.1)
        alienlaser_sound = pg.mixer.Sound('sounds/alienlaser.wav')
        alienlaser_sound.set_volume(0.1)
        photontorpedo_sound = pg.mixer.Sound('sounds/photon_torpedo.wav')
        photontorpedo_sound.set_volume(0.1)
        gameover_sound = pg.mixer.Sound('sounds/gameover.wav')
        gameover_sound.set_volume(0.1)
        self.sounds = {'alienlaser': alienlaser_sound, 'photontorpedo': photontorpedo_sound,
                       'gameover': gameover_sound}

        self.bg_music = bg_music


    def speed_up_music(self):
        # Use subprocess to call an external tool (e.g. sox) to speed up the music file
        # Replace "sox" with the name of the command-line tool you want to use
        subprocess.call(['sox', self.bg_music, 'temp_music.wav', 'tempo', '1.2'])

        # Load the modified music file
        pg.mixer.music.load('temp_music.wav')

        # Remove the temporary file
        os.remove('temp_music.wav')

    def reset_music_speed(self):
        pg.mixer.init(frequency=22050)
        pg.mixer.music.load(self.bg_music)
        pg.mixer.music.stop()
        pg.mixer.music.play()

    def play_bg(self):
        pg.mixer.music.play(-1, 0.0)

    def stop_bg(self):
        pg.mixer.music.stop()

    def shoot_laser(self, type): 
        pg.mixer.Sound.play(self.sounds['alienlaser' if type == LaserType.ALIEN else 'photontorpedo'])

    def gameover(self): 
        self.stop_bg() 
        pg.mixer.music.load('sounds/gameover.wav')
        self.play_bg()
        time.sleep(2.8)
