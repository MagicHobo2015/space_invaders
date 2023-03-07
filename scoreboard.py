import pygame.font

from ship import Ship


class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, game):
        """"Initialize scorekeeping attributes"""
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats
        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def save_high_score(self):
        """Save the high score to a file."""
        high_score_file = "high_score.txt"
        with open(high_score_file, "w") as file:
            file.write(str(self.stats.high_score))

    def show_score(self):
        """Draw score,level, and ships to the screen."""
        score_label = self.font.render("Score: ", True, self.text_color, self.settings.bg_color)
        high_score_label = self.font.render("High Score: ", True, self.text_color, self.settings.bg_color)
        self.screen.blit(high_score_label, (self.screen_rect.centerx - 270, 20))
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        for ship in self.ships:
            ship.draw()

    def update_score_text(self):
        """Update the score text based on the current score"""
        # Render the text surface with the score string
        score_str = f"Score: {self.stats.score}"
        self.score_text = self.score_font.render(score_str, True, (255, 255, 255))

        # Calculate the position of the text surface based on the position of the score image
        text_x = self.sb.score_rect.right - 100
        text_y = self.sb.score_rect.centery - self.score_text.get_height() / 2

        # Draw the text surface on the screen surface
        self.screen.blit(self.score_text, (text_x, text_y))


    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Center the high score at the top of teh screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right - 100
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = []
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = self.screen_rect.bottom - 10 - ship.rect.height
            self.ships.append(ship)
