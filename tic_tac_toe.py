import pygame
import sys


class TicTacToe:
    def __init__(self):
        """ initialize the game, and create its resources. """
        pygame.init()
        # Create the game screen into the display.
        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("Tic Tac Toe")

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
        self.screen.fill((250, 250, 250))

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # make the game instance and run it
    ttt = TicTacToe()
    ttt.run_game()
