import pygame
from settings import *


# class Wall(pygame.sprite.Sprite):
#     def __init__(self, wall_sprites, x, y, w, h):
#         self.groups = wall_sprites
#         pygame.sprite.Sprite.__init__(self, self.groups)
#         # self.image = pygame.Surface((TILESIZE, TILESIZE))
#         # self.image = pygame.image.load("img/map/box.png").convert_alpha()
#         # self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
#         # self.rect = self.image.get_rect(x, y, w, h)
#         self.rect = pygame.Rect(x,y,w,h)
#         self.x = x
#         self.y = y
#         self.rect.x = self.x
#         self.rect.y = self.y


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, wall_sprites, x, y, w, h):
        self.groups = wall_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.rect = pygame.Rect(x, y, w, h)
        self.hit_rect = self.rect
        # self.x = x
        # self.y = y
        self.rect.w = w
        self.rect.h = h
        self.rect.x = x
        self.rect.y = y

