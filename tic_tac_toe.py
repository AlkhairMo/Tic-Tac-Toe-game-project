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

        # Manage marker position
        self.marker = []

        for x in range(3):
            row = [0] * 3
            self.marker.append(row)

        # Player row 1 for X, -1 for O
        self.player = 1

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
                x_pos = mouse_pos[0]
                y_pos = mouse_pos[1]
                self._switch_turn(x_pos, y_pos)

    def _switch_turn(self, x_pos, y_pos):
        """ Switch players each time a player play. """
        if 50 < x_pos < 650 and 150 < y_pos < 750:
            if self.marker[(x_pos - 50) // 200][(y_pos - 150) // 200] == 0:
                self.marker[(x_pos - 50) // 200][(y_pos - 150) // 200] = self.player
                self.player *= -1
                # switch color to know the turn.
                if self.player == 1:
                    turn_color = 1
                else:
                    turn_color = 0
                self.settings.bg_color = self.settings.bg_colors[turn_color]

    def draw_icons(self):
        """ Draw X and O in position player want. """
        x_pos = 0
        for x in self.marker:
            y_pos = 0
            for y in x:
                if y == 1:
                    self.x_icon.rect = (((x_pos * 200) + 60), ((y_pos * 200) + 155))
                    self.x_icon.blitme()
                if y == -1:
                    self.O_icon.rect = (((x_pos * 200) + 60), ((y_pos * 200) + 155))
                    self.O_icon.blitme()
                y_pos += 1
            x_pos += 1

    def _update_screen(self):
        """ Update images on the screen and flip to new screen. """
        self.screen.fill(self.settings.bg_color)

        self.grid.blitme()

        self.draw_icons()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # make the game instance and run it
    ttt = TicTacToe()
    ttt.run_game()
