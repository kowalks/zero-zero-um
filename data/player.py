import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x,y):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y


    def update(self):
        self.rect.x = self.x*TILESIZE
        self.rect.y = self.y*TILESIZE

    def horizontal(self, sinal):
        self.x += sinal

    def vertical(self, sinal):
        self.y += sinal
