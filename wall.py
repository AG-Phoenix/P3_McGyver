"""  Module containing the Wall class. """

import pygame


class Wall(pygame.sprite.Sprite):
    """Initialize a Wall sprite. Extends pygame's Sprite class."""

    def __init__(self, y_pos, x_pos):
        """Initialize a Wall.

        :param y_pos: wall position on the y axis.
        :param x_pos: wall position on the x axis.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/wall.png")
        self.rect = self.image.get_rect()
        self.rect.x = x_pos * 32
        self.rect.y = y_pos * 32
