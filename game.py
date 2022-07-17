""" Modules containing the Game class."""
import sys
import pygame
from character import Character
from player import Player
from map import Map


class Game:
    """Class handling every actions inherent to the game itself."""

    def __init__(self):
        """Initialize a game.

        Creates a sprite group containing the player and the guard.
        Initialize the game map.
        Initialize pygame.
        """

        pygame.init()
        # Size of the game window (set to contain 15 tiles in width and height)
        self.game_window = pygame.display.set_mode((480, 522))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("McGyver's great escape")
        self.all_sprites = pygame.sprite.Group()
        self.map = Map("testmap.txt")
        self.player = Player(self.map.player_position)
        self.guard = Character(self.map.guard_position)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.guard)
        self.victory = False

    def draw_text(self, text, font_name, size, color, x_pos, y_pos):
        """Draws text on game window.

        :param text: Text to be written.
        :param font_name: Font used.
        :param size: Size of the text.
        :param color: Color of the text.
        :param x_pos: Text position on the x axis.
        :param y_pos: Text postion on the y axis.
        """

        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x_pos, y_pos)
        self.game_window.blit(text_surface, text_rect)

    def draw_sprites(self):
        """draws all sprites from all sprite groups."""

        self.game_window.fill((40, 40, 40))
        self.map.walls.draw(self.game_window)
        self.map.items.draw(self.game_window)
        self.all_sprites.draw(self.game_window)
        self.draw_text("Inventory", "fonts/dealerplate_california.ttf", 30,
                       (255, 255, 255), 320, 505)
        self.player.inventory.draw(self.game_window)

    def show_start_screen(self):
        """Shows the starting screen and waits for the user input."""

        self.game_window.fill((40, 40, 40))
        self.draw_text("McGyver", "fonts/Shanella.ttf", 100, (255, 255, 255),
                       240, 150)
        self.draw_text("The Great Escape", "fonts/Shanella.ttf", 100,
                       (255, 255, 255), 240, 250)
        self.draw_text("Press any key to start",
                       "fonts/dealerplate_california.ttf", 30, (205, 205, 205),
                       480 / 2, 522 * 3 / 4)
        pygame.display.flip()
        self.wait_for_user_input()

    def show_victory_screen(self):
        """Shows the victory screen at the end of a game."""

        self.game_window.fill((40, 40, 40))
        self.draw_text("VICTORY!", "fonts/dealerplate_california.ttf", 100,
                       (0, 255, 0), 240, 150)
        self.draw_text("Congratulations!", "fonts/Shanella.ttf", 100,
                       (255, 255, 255), 240, 250)
        self.draw_text("Press any key to start",
                       "fonts/dealerplate_california.ttf", 30, (205, 205, 205),
                       480 / 2, 522 * 3 / 4)
        pygame.display.flip()
        self.wait_for_user_input()

    def show_defeat_screen(self):
        """Show the defeat screen at the end of a game."""

        self.game_window.fill((40, 40, 40))
        self.draw_text("DEFEAT!", "fonts/dealerplate_california.ttf", 100,
                       (255, 0, 0), 240, 150)
        self.draw_text("Better luck next time!", "fonts/Shanella.ttf", 80,
                       (255, 255, 255), 240, 250)
        self.draw_text("Press any key to try again",
                       "fonts/dealerplate_california.ttf", 30, (205, 205, 205),
                       480 / 2, 522 * 3 / 4)
        pygame.display.flip()
        self.wait_for_user_input()

    def wait_for_user_input(self):
        """Wait for the user input during starting, defeat and victory screens.
        """

        pygame.event.wait()
        waiting = True
        while waiting:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pygame.KEYUP:
                    waiting = False
        self.play()

    def playing_loop(self):
        """Main playing loop. Game ends if player collides with the guard and
        has collected all items.
        """

        keep_playing = True
        while keep_playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
            self.game_window.fill((255, 255, 255))
            self.draw_sprites()
            collisions = pygame.sprite.spritecollide(self.player,
                                                     self.map.items, True)
            if collisions:
                for item in collisions:
                    self.player.pick_item(item)
            if pygame.sprite.collide_rect(self.player, self.guard):
                if not self.map.items:
                    self.victory = True
                keep_playing = False
            self.player.update(self.map.walls)
            pygame.display.update()
            self.clock.tick(60)

    def quit(self):
        """Quits the program."""

        pygame.quit()
        sys.exit()

    def play(self):
        """Starts a game and launches the playing loop."""

        self.__init__()
        self.playing_loop()
        if self.victory:
            self.show_victory_screen()
        else:
            self.show_defeat_screen()
