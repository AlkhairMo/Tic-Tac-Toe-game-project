import pygame
import sys

from settings import Settings
from grid import Grid
from X_icon import X
from O_icon import O


class TicTacToe:
    def __init__(self):
        """ initialize the game, and create its resources. """
        pygame.init()
        self.settings = Settings()
        # Create the game screen into the display.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Tic Tac Toe")

        self.grid = Grid(self)
        self.x_icon = X(self)
        self.O_icon = O(self)

        self.show_x = False

    def run_game(self):
        """ The main loop of the game."""
        while True:
            self._update_screen()
            self._check_events()

    def _check_events(self):
        """ Respond to user events(mouse and keyboard presses). """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_player_X(mouse_pos)
                self.show_x = True

    def _check_player_X(self, mouse_pos):
        """ Check mouse clicks of player 1. """
        if self.grid.rect.collidepoint(mouse_pos):
            self.x_icon.rect.center = self.grid.rect.center

    def _update_screen(self):
        """ Update images on the screen and flip to new screen. """
        self.screen.fill(self.settings.bg_color)

        self.grid.blitme()
        self.O_icon.blitme()

        if self.show_x:
            self.x_icon.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # make the game instance and run it
    ttt = TicTacToe()
    ttt.run_game()
