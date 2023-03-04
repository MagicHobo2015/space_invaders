import pygame as pg, sys, time
import pygame.sprite
import sys

from vector import Vector
from sound import Sound
from settings import Settings
from ship import Ship
from laser import Lasers
from alien import Aliens
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.window_height, self.window_width = self.settings.screen_height, self.settings.screen_width
        self.screen = pg.display.set_mode((self.window_width, self.window_height), 0, 32)
        pg.display.set_caption('Alien Invasion')
        self.speed = 3
        self.finished = False

        self.sound = Sound()
        self.sound.play_background()
        self.stats = GameStats(game=self)  # Create an instance to store game statistics
        self.ship = Ship(game=self)
        self.lasers = Lasers(game=self)
        self.ship.set_lasers(self.lasers)
        self.aliens = Aliens(game=self)

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # Make the Play button.
        self.play_button = Button(self, "Play")

        # Create an instance to store game statistics
        # and create a scoreboard
        self.sb = Scoreboard(self)

    def handle_events(self):
        up, down, left, right = Vector(0, -1), Vector(0, 1), Vector(-1, 0), Vector(1, 0)
        keys_dir = {pg.K_w: up, pg.K_UP: up,
                    pg.K_s: down, pg.K_DOWN: down,
                    pg.K_a: left, pg.K_LEFT: left,
                    pg.K_d: right, pg.K_RIGHT: right}

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game_over()
            elif event.type == pg.KEYDOWN:
                key = event.key
                if key in keys_dir:
                    self.ship.v = self.speed * keys_dir[key]
                elif key == pg.K_SPACE:
                    self.sound.play_laser()
                    self.ship.open_fire()
            elif event.type == pg.KEYUP:
                key = event.key
                if key in keys_dir:
                    self.ship.v = Vector()
                elif key == pg.K_SPACE:
                    self.ship.cease_fire()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)

    def check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        if self.play_button.rect.collidepoint(mouse_pos):
            # Reset the game statistics.
            self.stats.reset_stats()
            self.game_active = True

            # Get rid of any remaining bullets and aliens.
            self.lasers.lasers.empty()
            self.aliens.aliens.empty()

            self.sb.prep_level()
            self.sb.prep_ships()

            # Create a new fleet and center the ship.
            self.aliens.create_fleet()
            self.ship.center_ship()
            self.settings.initialize_dynamic_settings()

    def update_lasers(self):
        # Get rid of bullets that have disappeared.
        for laser in self.lasers.lasers.copy():
            if laser.rect.bottom <= 0:
                self.lasers.lasers.remove(laser)
        self.check_lasers_alien_collision()

    def check_lasers_alien_collision(self):
        '''Respond to laser-alien collisions'''
        # Remove any lasers and aliens that have collided.
        collisions = pygame.sprite.groupcollide(self.lasers.lasers, self.aliens.aliens, True, True)
        if collisions:
            self.sound.play_alien_explo()
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens.aliens:  # Destroy existing bullets and create new fleet
            self.lasers.lasers.empty()
            self.aliens.create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def update_aliens(self):
        self.aliens.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens.aliens):  # takes two arguments: a sprite and a group.
            self.ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self.check_aliens_bottom()

    def ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            self.sound.play_ship_explo()
            # Decrement ships_left and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining bullets and aliens.
            self.lasers.lasers.empty()
            self.aliens.aliens.empty()

            # Create a new fleet and center the ship.
            self.aliens.create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)

        else:
            self.finished = False  # Ends the game

    def check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self.ship_hit()
                break

    def restart(self):
        pass

    def game_over(self):
        self.finished = True
        self.sound.play_gameover()
        self.sound.stop_background()
        self.sb.save_high_score()
        pg.quit()
        sys.exit()

    def play_again(self):
        pass

    def play(self):

        self.play_button = Button(self, "Play")

        while not self.finished:
            self.handle_events()

            self.sb.show_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            if not self.game_active:
                self.play_button.draw_button()

            if self.play_button.rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
                # Reset the game statistics()
                self.stats.reset_stats()
                self.game_active = True

                self.lasers.lasers.empty()
                self.aliens.aliens.empty()

                self.aliens.create_fleet()
                self.ship.center_ship()

            if self.game_active:
                # If the game is active, update the ship, lasers, and aliens.
                self.screen.fill(self.settings.bg_color)
                self.sb.show_score()
                self.sb.prep_level()
                self.sb.prep_ships()
                self.ship.update()
                self.lasers.update()
                self.aliens.update()
                self.update_lasers()
                self.update_aliens()
            pg.display.update()
            # time.sleep(0.02)


def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()
