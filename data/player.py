import pygame
from settings import *

class Character(pygame.sprite.Sprite):
    def __init__(self, x=0, y = 0, hp = 100, COLOR = RED):
        self.life = hp
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(COLOR)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
    def update(self):
        self.rect.x = self.x*TILESIZE
        self.rect.y = self.y*TILESIZE

    def check_move(self, sinalx, sinaly, walls):
        Collide = False
        for brick in walls:
            if (self.x == brick.x and self.y == brick.y):
                Collide = True
        if Collide == True:
            self.x -= sinalx;
            self.y -= sinaly;

    def move(self, sinalx, sinaly, walls):
        self.x += sinalx
        self.y += sinaly
        self.check_move(sinalx, sinaly, walls)




class Player(Character):
    def __init__(self, x,y, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image.fill(YELLOW)
        self.x = x;
        self.y = y;

class Enemy(Character):
    def __init__(self, x,y, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image.fill(GREEN)
        self.x = x;
        self.y = y;

