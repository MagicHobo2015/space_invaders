import colors

from colors import LIGHT_GREY, DARK_GREY, LIGHT_RED, RED, BLACK


class Settings:
    def __init__(self):
        self.screen_width, self.screen_height = 1200, 800
        self.bg_color = LIGHT_RED

        self.ship_image = 'images/ship.bmp'
        self.ship_speed = 3
        self.ship_limit = 3

        self.alien_image = 'images/alien.bmp'
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 5

        self.laser_speed_factor = 1.2
        self.laser_width = 10
        self.laser_height = 50
        self.lasers_allowed = 2
        self.laser_color = RED

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien points values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.laser_speed_factor = 2.5
        self.alien_speed_factor = 1.0

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.laser_speed_factor += self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

