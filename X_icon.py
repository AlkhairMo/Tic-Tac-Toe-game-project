import pygame
from grid import Grid


class X:
    """ Draw x icon in the screen. """
    def __init__(self, ttt_game):
        """ Initialize the x icon. """
        self.grid = Grid(ttt_game)
        self.screen = ttt_game.screen
        self.settings = ttt_game.settings
        self.grid_rect = self.grid.rect

        self.image = pygame.image.load("images/X.png")
        self.image = pygame.transform.scale(self.image, (180, 180))
        self.rect = self.image.get_rect()
        self.rect.center = self.grid_rect.center

    def blitme(self):
        """ Draw x icon in the screen"""
        self.screen.blit(self.image, self.rect)

