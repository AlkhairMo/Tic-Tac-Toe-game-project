import pygame
from grid import Grid


class O:
    """ Draw O icon in the screen. """
    def __init__(self, ttt_game):
        """ Initialize the O icon. """
        self.grid = Grid(ttt_game)
        self.screen = ttt_game.screen
        self.grid_rect = self.grid.rect

        self.image = pygame.image.load("images/O.png")
        self.image = pygame.transform.scale(self.image, (170, 170))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.grid_rect.topleft

    def blitme(self):
        """ Draw o icon in the screen"""
        self.screen.blit(self.image, self.rect)

