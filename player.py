""" Module containing the Player class."""

import pygame
from character import Character


class Player(Character):
    """Class handling actions inherent to the player."""

    def __init__(self, position):
        """Initialize player by extending class Character, adding an inventory.

        :param position: Player position
        """

        Character.__init__(self, position)
        self.inventory = pygame.sprite.Group()
        self.image = pygame.image.load("sprites/mcgyver.png")
        self.rect = self.image.get_rect()
        self.x_pos = position[1] * 32
        self.y_pos = position[0] * 32
        # Speed at which player moves.
        self.speed = 3

    def get_keys(self, velocity_x, velocity_y):
        """Gets keys pressed by user to know which way they whish to go.

        :param velocity_x: speed on the x axis.
        :param velocity_y: speed on the y axis.
        """

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            velocity_x = -self.speed
        if keys[pygame.K_RIGHT]:
            velocity_x = self.speed
        if keys[pygame.K_UP]:
            velocity_y = -self.speed
        if keys[pygame.K_DOWN]:
            velocity_y = self.speed
        # Makes sure player velocity stays the same if going diagonally.
        if velocity_x != 0 and velocity_y != 0:
            velocity_x *= 0.7071
            velocity_y *= 0.7071
        return velocity_x, velocity_y

    def collide_with_walls(self, direction, walls, velocity_x, velocity_y):
        """ Tests if player is colliding with a wall preventing him from
        moving past that wall.

        collisions are tested on the y and x axis separately to prevents
        graphical glitches where player sprite would not be in contact of a
        wall despite colliding with it and allow to keep moving when colliding
        with a wall while moving diagonally.

        :param direction: direction player is heading towards.
        :param walls: contains all the walls.
        :param velocity_x: speed on the x axis.
        :param velocity_y: speed on the y axis.
        """

        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, walls, False)
            if hits:
                if velocity_x > 0:
                    self.x_pos = hits[0].rect.left - self.rect.width
                if velocity_x < 0:
                    self.x_pos = hits[0].rect.right
                velocity_x = 0
                self.rect.x = self.x_pos
        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, walls, False)
            if hits:
                if velocity_y > 0:
                    self.y_pos = hits[0].rect.top - self.rect.height
                if velocity_y < 0:
                    self.y_pos = hits[0].rect.bottom
                velocity_y = 0
                self.rect.y = self.y_pos

    def update(self, walls):
        """Inherited from Sprite class. Updates the player status.

        :param walls: contains all the walls.
        """

        velocity_x = 0
        velocity_y = 0
        velocity_x, velocity_y = self.get_keys(velocity_x, velocity_y)
        self.x_pos += velocity_x
        self.y_pos += velocity_y
        self.rect.x = self.x_pos
        self.collide_with_walls('x', walls, velocity_x, velocity_y)
        self.rect.y = self.y_pos
        self.collide_with_walls('y', walls, velocity_x, velocity_y)

    def pick_item(self, item):
        """ Adds item to the inventory by placing it in the inventory instead
        of inside the map.
        """

        item.rect.y = 485
        item.rect.x = 352 + (len(self.inventory) + 1) * 32
        self.inventory.add(item)
