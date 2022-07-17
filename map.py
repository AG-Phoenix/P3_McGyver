"""  Module containing the Map class. """

import pygame
from item import Item
from wall import Wall


class Map:
    """Class handling actions inherent to the game map."""

    def __init__(self, file_name):
        """Creates a map from a text file.

        Stores all empty_spots, player and guard position as well as the walls
        in a sprite group and the items in a separate sprite group.

        :param file_name: Name of text file containing the map layout.
        """

        self.walls = pygame.sprite.Group()
        self.empty_spots = list()
        self.items = pygame.sprite.Group()
        self.player_position = list()
        self.guard_position = list()
        self.read_file(file_name)
        self.create_items()

    def create_items(self):
        """Creates item instances and stores them in a list."""

        needle = Item(self.empty_spots, "sprites/needle.png")
        self.items.add(needle)
        ether = Item(self.empty_spots, "sprites/ether.png")
        self.items.add(ether)
        tube = Item(self.empty_spots, "sprites/tube.png")
        self.items.add(tube)

    def read_file(self, file_name):
        """Reads a file to extract the map layout out of it.

        :param file_name: Name of the file to be read.
        """

        with open(file_name, 'r') as map_file:
            for y_count, line in enumerate(map_file):
                for x_count, letter in enumerate(line):
                    if letter == "M":
                        self.player_position = [y_count, x_count]
                    elif letter == "G":
                        self.guard_position = [y_count, x_count]
                    elif letter == '#':
                        self.walls.add(Wall(y_count, x_count))
                    elif letter == " ":
                        self.empty_spots.append([y_count, x_count])
