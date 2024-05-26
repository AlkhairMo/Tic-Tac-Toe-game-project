import pygame


class Grid:
    """ A class to draw the grid of the game into screen. """
    def __init__(self, ttt_game):
        """ Initialize grid. """
        self.ttt_game = ttt_game
        self.screen = ttt_game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("images/grid.jpg")
        self.image = pygame.transform.scale(self.image, (600, 600))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 150

    def blitme(self):
        self.screen.blit(self.image, self.rect)
