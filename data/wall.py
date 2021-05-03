import pygame
from settings import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, wall_sprites, x, y, w, h):
        self.groups = wall_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.rect = pygame.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.rect.w = w
        self.rect.h = h
        self.rect.x = x
        self.rect.y = y

