""" Modules containing the class Character """
import pygame


class Character(pygame.sprite.Sprite):
    """Class initializing a character sprite. Extends pygame Sprite class"""

    def __init__(self, position):
        """Initialize a Character with a position and an image to embody them.

        :param position: Position of the character.
        """

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/guard.png")
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.x = self.position[1] * 32
        self.rect.y = self.position[0] * 32
