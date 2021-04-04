import pygame
from settings import *

class Item(*args, **kwargs):
    def __init__(self, x=0, y = 0, got = False, COLOR = LIGHTGREY, *args, **kwargs):
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(COLOR)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.got = got
     
    def check_got(self, player):
      if (self.x == player.x and self.y == player.y):
        got = True
