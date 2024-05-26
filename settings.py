import random


class Settings:
    def __init__(self):
        """ initialize all game settings. """
        # Screen settings:
        self.screen_width = 700
        self.screen_height = 800
        self.bg_colors = [(56, 205, 255), (255, 102, 102)]
        self.bg_color = random.choice(self.bg_colors)
