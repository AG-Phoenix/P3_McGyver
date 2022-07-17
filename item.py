""" Module containing the Item class."""

from random import randrange
import pygame


class Item(pygame.sprite.Sprite):
    """Initialize an item sprite that needs to be picked by player to beat the
    guard. Extends pygame's Sprite class.
    """

    def __init__(self, empty_spots, item_image_path):
        """Creates an Item with a position picked randomly from all the empty
        spots left on the map and and image embodying it.

        :param item_image_path: Path of the item image.
        :param empty_spots: The list of all the empty spots in the map.
        """

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(item_image_path)
        self.rect = self.image.get_rect()
        self.position = (empty_spots.pop(randrange(len(empty_spots))))
        self.rect.x = self.position[1] * 32 + (self.rect.size[0]/2)
        self.rect.y = self.position[0] * 32
