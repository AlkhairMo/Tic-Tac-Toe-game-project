import pygame
import sys

from grid import Grid
from X_icon import X
from O_icon import O
from board import Board


class TicTacToe:
    def __init__(self):
        """ initialize the game, and create its resources. """
        pygame.init()
        # Create the game screen into the display.
        self.screen = pygame.display.set_mode((700, 800))
        pygame.display.set_caption("Tic Tac Toe")

        # Background colors
        self.bg_colors = [(56, 205, 255), (255, 102, 102), (102, 255, 102)]

        # line color
        self.line_color = (26, 26, 26)

        # Icons
        self.grid = Grid(self)
        self.x_icon = X(self)
        self.O_icon = O(self)
        self.winner_board = Board(self, "We have a winner!", "Play again")
        self.draw_board = Board(self, "It is draw", "Play again")

        self._prep_game()

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
                if self.game_playing:
                    self._switch_turn(x_pos, y_pos)
                self._play_again_button(mouse_pos)

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
                self.bg_color = self.bg_colors[turn_color]
                self._check_draw()

    def _play_again_button(self, mouse_pos):
        """ Make play again button work. """
        if not self.game_playing and (self.winner_board.play_again_image_rect.collidepoint(mouse_pos)
                                      or self.draw_board.play_again_image_rect.collidepoint(mouse_pos)):
            self._prep_game()

    def _prep_game(self):
        """ Prepare and est game settings for new game. """
        # Manage marker position
        self.marker = []
        for x in range(3):
            row = [0] * 3
            self.marker.append(row)

        # check draw list and flag.
        self.fulled_markers = []
        self.draw = False

        # Player turn 1 for X, -1 for O
        self.player = 1
        self.bg_color = self.bg_colors[1]

        # Winner variable
        self.winner = 0
        self.player_win = False

        # Game playing flag
        self.game_playing = True

    def draw_icons(self):
        """ Draw X and O in position player want. """
        x_pos = 0
        for x in self.marker:
            y_pos = 0
            for y in x:
                if y == 1:
                    self.x_icon.rect = (((x_pos * 200) + 65), ((y_pos * 200) + 160))
                    self.x_icon.blitme()
                if y == -1:
                    self.O_icon.rect = (((x_pos * 200) + 65), ((y_pos * 200) + 160))
                    self.O_icon.blitme()
                y_pos += 1
            x_pos += 1
            self._check_winner()

    def _check_winner(self):
        """ Checking one of the player had win. """
        y_pos = 0
        for x in self.marker:
            # check columns
            if sum(x) == 3:
                self._player_x_win()
                pygame.draw.line(self.screen, self.line_color,
                                 (150 + y_pos * 200, 170), (150 + y_pos * 200, 730), 6)
            if sum(x) == -3:
                self._player_o_win()
                pygame.draw.line(self.screen, self.line_color,
                                 (150 + y_pos * 200, 170), (150 + y_pos * 200, 730), 6)
            # check rows
            if self.marker[0][y_pos] + self.marker[1][y_pos] + self.marker[2][y_pos] == 3:
                self._player_x_win()
                pygame.draw.line(self.screen, self.line_color,
                                 (70, y_pos * 200 + 250), (630, y_pos * 200 + 250), 6)
            if self.marker[0][y_pos] + self.marker[1][y_pos] + self.marker[2][y_pos] == -3:
                self._player_o_win()
                pygame.draw.line(self.screen, self.line_color,
                                 (70, y_pos * 200 + 250), (630, y_pos * 200 + 250), 6)
            y_pos += 1
        # check crosses
        if self.marker[0][0] + self.marker[1][1] + self.marker[2][2] == 3:
            self._player_x_win()
            pygame.draw.line(self.screen, self.line_color, (100, 200), (600, 700), 6)
        if self.marker[0][2] + self.marker[1][1] + self.marker[2][0] == 3:
            self._player_x_win()
            pygame.draw.line(self.screen, self.line_color, (570, 220), (120, 680), 6)
        if self.marker[0][0] + self.marker[1][1] + self.marker[2][2] == -3:
            self._player_o_win()
            pygame.draw.line(self.screen, self.line_color, (100, 200), (600, 700), 6)
        if self.marker[0][2] + self.marker[1][1] + self.marker[2][0] == -3:
            self._player_o_win()
            pygame.draw.line(self.screen, self.line_color, (570, 220), (120, 680), 6)

    def _player_x_win(self):
        """ Set player X winning actions. """
        self.winner = 1
        self.game_playing = False
        self.bg_color = self.bg_colors[1]
        self.player_win = True

    def _player_o_win(self):
        """ Set player O winning actions. """
        self.winner = -1
        self.game_playing = False
        self.bg_color = self.bg_colors[0]
        self.player_win = True

    def _check_draw(self):
        """ Checking the grid is full and no one has win. """
        for row in self.marker:
            for element in row:
                if element != 0:
                    self.fulled_markers.append(element)
                if len(self.fulled_markers) == 45:
                    self.draw = True
                    self.game_playing = False

    def _update_screen(self):
        """ Update images on the screen and flip to new screen. """
        self.screen.fill(self.bg_color)

        self.grid.blitme()

        self.draw_icons()

        if not self.game_playing and self.player_win:
            self.winner_board.blitme()
        if not self.game_playing and not self.player_win and self.draw:
            self.draw_board.blitme()
            self.bg_color = self.bg_colors[2]

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # make the game instance and run it
    ttt = TicTacToe()
    ttt.run_game()
