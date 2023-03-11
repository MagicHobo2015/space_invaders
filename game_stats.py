import pygame as pg
import os
from settings import Settings


class GameStats:
    '''Track statistics for Alien Invasion.'''

    def __init__(self, game):
        """Initialize statistics."""
        self.settings = game.settings
        self.reset_stats()
        self.level = 1
        # High score should never be reset.
        # Load the high score from a file if it exists.
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """Load the high score from a file."""
        high_score_file = "high_score.txt"
        if os.path.exists(high_score_file):
            with open(high_score_file) as file:
                try:
                    high_score = int(file.read())
                except ValueError:
                    # If the file contains invalid data, use 0 as the high score
                    high_score = 0
        else:
            high_score = 0
        return high_score
