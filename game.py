import pygame as pg
from settings import Settings
from laser import Lasers, LaserType
from alien import Aliens
from ship import Ship
from sound import Sound
from scoreboard import Scoreboard
from vector import Vector
from barrier import Barriers
from button import Button
from game_stats import GameStats
import sys 


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height   # tuple
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Alien Invasion")

        self.finished = False
        self.game_active = False
        self.stats = GameStats(game=self)
        self.sound = Sound(bg_music="sounds/startrek.wav")
        self.scoreboard = Scoreboard(game=self)

        self.ship_lasers = Lasers(settings=self.settings, type=LaserType.SHIP)
        self.alien_lasers = Lasers(settings=self.settings, type=LaserType.ALIEN)
        
        self.barriers = Barriers(game=self)
        self.ship = Ship(game=self)
        self.aliens = Aliens(game=self)
        self.settings.initialize_speed_settings()
        self.score_font = pg.font.SysFont(None, 48)
        self.score_text = None
        self.title_menu()

    def handle_events(self):
        keys_dir = {pg.K_w: Vector(0, -1), pg.K_UP: Vector(0, -1), 
                    pg.K_s: Vector(0, 1), pg.K_DOWN: Vector(0, 1),
                    pg.K_a: Vector(-1, 0), pg.K_LEFT: Vector(-1, 0),
                    pg.K_d: Vector(1, 0), pg.K_RIGHT: Vector(1, 0)}
        
        for event in pg.event.get():
            if event.type == pg.QUIT: self.game_over()
            elif event.type == pg.KEYDOWN:
                key = event.key
                if key in keys_dir:
                    self.ship.v += self.settings.ship_speed * keys_dir[key]
                elif key == pg.K_SPACE:
                    self.ship.open_fire()
            elif event.type == pg.KEYUP:
                key = event.key
                if key in keys_dir:
                    self.ship.v = Vector()
                elif key == pg.K_SPACE:
                    self.ship.cease_fire()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if not self.game_active:
                    self.check_play_button(mouse_pos)

    def check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        if not self.game_active and self.play_button.rect.collidepoint(mouse_pos):
            # Reset the game statistics.
            self.stats.reset_stats()
            self.game_active = True

            # Get rid of any remaining bullets and aliens.
            self.ship_lasers.lasers.empty()
            self.alien_lasers.lasers.empty()
            self.aliens.aliens.empty()

            self.scoreboard.prep_level()

            # Create a new fleet and center the ship.
            self.aliens.create_fleet()
            self.ship.center_ship()
            self.settings.initialize_speed_settings()

    def update_score_text(self):
        """Update the score text based on the current score"""
        # Render the text surface with the score string
        score_str = f"Score: {self.scoreboard.score}"
        self.score_text = self.score_font.render(score_str, True, (0, 0, 0), self.settings.bg_color)

        # Calculate the position of the text surface based on the position of the score image
        text_x = self.scoreboard.score_rect.right - 200
        text_y = self.scoreboard.score_rect.centery - self.score_text.get_height() / 2

        # Draw the text surface on the screen surface
        self.screen.blit(self.score_text, (text_x, text_y))


    def reset(self):
        print('Resetting game...')
        # self.lasers.reset()    # handled by ship for ship_lasers and by aliens for alien_lasers
        self.barriers.reset()
        self.ship.reset()
        self.aliens.reset()
        self.scoreboard.reset()

    def game_over(self):
        print('All ships gone: game over!')
        self.finished = True
        self.sound.gameover()
        self.sound.stop_bg()
        self.scoreboard.save_high_score()
        pg.quit()
        sys.exit()

    def title_menu(self):

        # create a font object
        self.screen.fill(self.settings.title_bg_color)
        space_font = pg.font.SysFont(None, 200)
        invaders_font = pg.font.SysFont(None, 150)
        points_font = pg.font.SysFont(None, 50)

        # create text
        space_text = space_font.render("SPACE", True, self.settings.title_space_text)
        invaders_text = invaders_font.render("INVADERS", True, self.settings.title_invaders_text)

        space_text_rect = space_text.get_rect(center=self.screen.get_rect().center)
        invaders_text_rect = invaders_text.get_rect(center=self.screen.get_rect().center)

        # Adjust positions
        space_text_rect.centery -= 295
        invaders_text_rect.centery += -195

        # display the text on the screen
        self.screen.blit(space_text, space_text_rect)
        self.screen.blit(invaders_text, invaders_text_rect)
        
        # just hold the alien image info here.
        self.alien_one = ['images/alien__00.png', 'images/alien__01.png']
        self.alien_two = ['images/alien__10.png', 'images/alien__11.png']
        self.alien_three = ['images/alien__20.png', 'images/alien__21.png']
        self.motherShip = 'images/motherShip.png'
        

        # Load and display alien sprites along with their points string
        alien_one_image = pg.image.load(self.alien_one[0]).convert_alpha()
        alien_one_rect = alien_one_image.get_rect()
        alien_one_rect.centerx = self.screen.get_rect().centerx - 100  # Move to the left by 100
        alien_one_rect.top = invaders_text_rect.bottom + 50   # below the "INVADERS" text from the title screen
        self.screen.blit(alien_one_image, alien_one_rect)
        alien_one_points_text = points_font.render("= 10 points", True, (255, 255, 255)) # points string
        alien_one_points_rect = alien_one_points_text.get_rect()
        alien_one_points_rect.left = alien_one_rect.right + 10
        alien_one_points_rect.centery = alien_one_rect.centery
        self.screen.blit(alien_one_points_text, alien_one_points_rect)

        alien_two_image = pg.image.load(self.alien_two[0]).convert_alpha()
        alien_two_rect = alien_two_image.get_rect()
        alien_two_rect.centerx = self.screen.get_rect().centerx - 100
        alien_two_rect.top = invaders_text_rect.bottom + 125
        self.screen.blit(alien_two_image, alien_two_rect)
        alien_two_points_text = points_font.render("= 20 points", True, (255, 255, 255))
        alien_two_points_rect = alien_two_points_text.get_rect()
        alien_two_points_rect.left = alien_two_rect.right + 10
        alien_two_points_rect.centery = alien_two_rect.centery
        self.screen.blit(alien_two_points_text, alien_two_points_rect)

        alien_three_image = pg.image.load(self.alien_three[0]).convert_alpha()
        alien_three_rect = alien_three_image.get_rect()
        alien_three_rect.centerx = self.screen.get_rect().centerx - 100
        alien_three_rect.top = invaders_text_rect.bottom + 200
        self.screen.blit(alien_three_image, alien_three_rect)
        alien_three_points_text = points_font.render("= 30 points", True, (255, 255, 255))
        alien_three_points_rect = alien_three_points_text.get_rect()
        alien_three_points_rect.left = alien_three_rect.right + 10
        alien_three_points_rect.centery = alien_three_rect.centery
        self.screen.blit(alien_three_points_text, alien_three_points_rect)

        mother_ship_image = pg.transform.rotozoom(pg.image.load(self.motherShip).convert_alpha(), 0, 2.5)
        mother_ship_rect = mother_ship_image.get_rect()
        mother_ship_rect.centerx = self.screen.get_rect().centerx - 100
        mother_ship_rect.top = invaders_text_rect.bottom + 275
        self.screen.blit(mother_ship_image, mother_ship_rect)
        mother_ship_points_text = points_font.render("= ??? points", True, (255, 255, 255))
        mother_ship_points_rect = mother_ship_points_text.get_rect()
        mother_ship_points_rect.left = mother_ship_rect.right + 10
        mother_ship_points_rect.centery = mother_ship_rect.centery
        self.screen.blit(mother_ship_points_text, mother_ship_points_rect)

        # create a Play button and position it on the screen
        self.play_button = Button(self, "Play")
        self.play_button.rect.centerx = self.screen.get_rect().centerx
        self.play_button.rect.bottom = self.screen.get_rect().bottom + 300

        # update the display
        pg.display.flip()

    def play(self):
        self.sound.play_bg()
        self.play_button = Button(self, "Play")

        while not self.finished:
            self.handle_events()

            if not self.game_active:
                self.play_button.draw_button()

            if self.play_button.rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
                # Reset the game statistics()
                self.stats.reset_stats()
                self.game_active = True

                self.ship_lasers.lasers.empty()
                self.alien_lasers.lasers.empty()
                self.update_score_text()

            if self.game_active:
                self.screen.fill(self.settings.bg_color)
                self.ship.update()
                self.aliens.update()
                self.barriers.update()
                # self.lasers.update()    # handled by ship for ship_lasers and by alien for alien_lasers
                self.scoreboard.update()
                self.scoreboard.show_score()
                self.scoreboard.prep_level()
                self.scoreboard.prep_score()
                self.update_score_text()
                self.ship.draw_ship_lives()
            pg.display.flip()


def main():
    g = Game()
    g.play()

if __name__ == '__main__':
    main()
