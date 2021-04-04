import pygame
from settings import *

class Wall(pygame.sprite.Sprite):
    def __init__(self, all_sprites, wall_sprites, x, y):
        self.groups = all_sprites, wall_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y =y
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE



