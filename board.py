import pygame


class Board:
    def __init__(self, ttt_game, winner_text, play_again_text):
        """ Initialize the board of game actions. """
        self.screen = ttt_game.screen

        self.font = pygame.font.SysFont(None, 46)
        self.text_color = (30, 30, 30)
        self.board_bg_color = (225, 225, 225)
        self.play_again_bg_color = (0, 225, 0)
        self.board_rect = pygame.Rect(200, 50, 300, 90)
        self.prep_board(winner_text, play_again_text)

    def prep_board(self, winner_text, play_again_text):
        """ Prepare the image of board. """
        self.winner_image = self.font.render(winner_text, True,
                                             self.text_color, self.board_bg_color)
        self.winner_image_rect = self.winner_image.get_rect()
        self.winner_image_rect.midtop = self.board_rect.midtop
        self.play_again_image = self.font.render(play_again_text, True,
                                                 self.text_color, self.play_again_bg_color)
        self.play_again_image_rect = self.play_again_image.get_rect()
        self.play_again_image_rect.y = 95
        self.play_again_image_rect.centerx = self.board_rect.centerx

    def blitme(self):
        self.screen.fill(self.board_bg_color, self.board_rect)
        self.screen.blit(self.winner_image, self.winner_image_rect)
        self.screen.blit(self.play_again_image, self.play_again_image_rect)
