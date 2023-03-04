import pygame as pg
from pygame.sprite import Sprite, Group
from vector import Vector


class Aliens:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.ship = game.ship
        self.settings = game.settings
        self.aliens = Group()  # Initializes group object to hold the fleet of aliens
        self.add(Alien(game=game))    # will change to add a bunch of Alien's
        self.v = Vector(self.settings.alien_speed_factor, 0)  # Vector object to control the speed and direction of the
        # aliens and the movement,
        self.create_fleet()

    def add(self, alien): self.aliens.add(alien)

    def create_fleet(self):  #
        alien = Alien(game=self.game) # create an instance of an Alien
        number_aliens_x = self.get_number_aliens_x(alien.rect.width)
        number_rows = self.get_number_rows(self.ship.rect.height,
                                           alien.rect.height)
        for row_number in range(number_rows):
            self.create_row(number_aliens_x, row_number)

    def create_row(self, number_aliens_x, row_number):  # creates a series of alien objects using create_alien() method
        # passing in the row number and the alien number within the row.
        for n in range(number_aliens_x):
            self.create_alien(n=n, row_number=row_number)

    def get_number_aliens_x(self, alien_width): # Used to calculate the number of aliens tha can fit in a row and the
        # number of rows that wil fit on the screen, respectively.
        available_space_x = self.settings.screen_width - 1.2 * alien_width
        number_aliens_x = int(available_space_x / (1.2 * alien_width))
        return number_aliens_x

    def create_alien(self, n, row_number):
        alien = Alien(game=self.game)
        alien.x = alien.rect.width * (1.2 * n + 1)  # x position
        alien.y = alien.rect.height * (1.2 * row_number + 1)  # y position
        alien.rect.x, alien.rect.y = alien.x, alien.y
        self.add(alien)

    def get_number_rows(self, ship_height, alien_height): # Used to calculate the number of aliens tha can fit in a row
        # and the number of rows that wil fit on the screen, respectively.
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = int(available_space_y / (1.2 * alien_height))
        return number_rows

    def reverse_fleet(self): # is called when the fleet of aliens reaches the edge of the screen. It changes the
        # direction of the aliens' movement and drops them down one row
        self.v.x *= -1
        for alien in self.aliens:
            alien.v.x *= -1
            alien.y += self.settings.fleet_drop_speed

    def check_edges(self): # Use to determine if the fleet of aliens has reached the dge of the screen or the
        # bottom of the screen or the edge of the screen
        for alien in self.aliens:
            if alien.check_edges(): return True
        return False

    def check_bottom(self):
        for alien in self.aliens:
            if alien.rect.bottom >= self.settings.screen_height: return True
        return False

    def update(self): # responsible for updating the position of the aliens and checking for collisions.
        # is called every frame. The game_over() method is called to end the game.
        for alien in self.aliens: alien.update()
        if self.check_bottom():
            self.game.game_over()
        if self.check_edges():
            self.reverse_fleet()
        self.draw() # pygame draws each element in the group at the position defined by its rect attribute.

    def draw(self): # is used to draw the alien on the screen
        for alien in self.aliens: alien.draw()


class Alien(Sprite):  # Subclass of pygame Sprite class. This is responsible for creating and updating individual alien
    # object as a parameter and initializes several attributes, including the aliens image, position, and speed.
    def __init__(self, game):  # It takes in the same 'game' object as a parameter
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.ship = game.ship
        self.v = Vector(game.settings.alien_speed_factor, 0)  # speed setting

        self.image = pg.image.load(self.settings.alien_image)
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = self.rect.width, self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):  # Is used to determine if the alien has reached the edge opf the screen and needs to change
        # direction.
        return self.rect.left <= 0 or self.rect.right >= self.settings.screen_width

    def change_direction(self): self.v.x *= -1  # changes the direction of the alien's movement.

    def update(self):  # updates the position of the alien based on its speed and direction.
        self.y += self.v.y
        self.x += self.v.x
        self.rect.x, self.rect.y = self.x, self.y

    def draw(self): self.screen.blit(self.image, self.rect)  # draws the alien on the screen.
