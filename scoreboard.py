import pygame as pg 
# import pygame.font

from ship import Ship


class Scoreboard:
    def __init__(self, game): 
        self.score = 0
        self.level = 0
        self.high_score = 0

        self.game = game
        self.stats = game.stats
        
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.text_color = (0, 0, 0)
        self.font = pg.font.SysFont(None, 48)

        self.score_image = None 
        self.score_rect = None
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def save_high_score(self):
        """Save the high score to a file."""
        high_score_file = "high_score.txt"
        with open(high_score_file, "w") as file:
            file.write(str(self.stats.high_score))

    def increment_score(self): 
        self.score += self.settings.alien_points
        self.prep_score()
        self.check_high_score()

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right - 70
        self.level_rect.top = self.score_rect.bottom + 10

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.score > self.stats.high_score:
            self.stats.high_score = self.score
            self.prep_high_score()

    def prep_score(self): 
        score_str = str(self.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Center the high score at the top of teh screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Draw score,level, and ships to the screen."""
        score_label = self.font.render("Score: ", True, self.text_color, self.settings.bg_color)
        high_score_label = self.font.render("High Score: ", True, self.text_color, self.settings.bg_color)
        level_label = self.font.render("Level: ", True, self.text_color, self.settings.bg_color)
        self.screen.blit(high_score_label, (self.screen_rect.centerx - 270, 20))
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(level_label, (self.level_rect.centerx - 115, self.level_rect.y))

    def reset(self): 
        self.score = 0
        self.update()

    def update(self): 
        # TODO: other stuff
        self.draw()

    def draw(self): pass   # I already have a score printing out in game.py
       #self.screen.blit(self.score_image, self.score_rect)

