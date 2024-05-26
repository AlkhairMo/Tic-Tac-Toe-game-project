import pygame
import sys

from settings import Settings
from grid import Grid


class TicTacToe:
    def __init__(self):
        """ initialize the game, and create its resources. """
        pygame.init()
        self.settings = Settings()
        # Create the game screen into the display.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Tic Tac Toe")

        self.grid = Grid(self)

    def run_game(self):
        """ The main loop of the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """ Respond to user events(mouse and keyboard presses). """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        self.grid.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # make the game instance and run it
    ttt = TicTacToe()
    ttt.run_game()
