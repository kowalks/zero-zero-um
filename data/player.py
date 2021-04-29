import pygame
from settings import *
vec = pygame.math.Vector2

class Character(pygame.sprite.Sprite):
    def __init__(self, x=0, y = 0, hp = 100, COLOR = RED):
        self.life = hp
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(COLOR)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def update(self):
        self.x = self.rect.x/TILESIZE
        self.y = self.rect.y*TILESIZE

    def check_move(self, sinalx, sinaly, walls):
        collide = False
        for brick in walls:
            if (self.x == brick.x and self.y == brick.y):
                collide = True
        if collide:
            self.rect.x -= sinalx
            self.rect.y -= sinaly

    def move(self, sinalx, sinaly, walls):
        self.rect.x += sinalx * PLAYER_SPEED
        self.rect.y += sinaly * PLAYER_SPEED
        if sinalx == 1:
           self.image = self.image_r
        elif sinalx == -1:
           self.image = self.original_image

        self.check_move(sinalx, sinaly, walls)


class Player(Character):
    def __init__(self, x,y, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_image = pygame.image.load("img/player/player.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (TILESIZE, TILESIZE))
        self.image_r = pygame.image.load("img/player/player_right.png").convert_alpha()
        self.image_r = pygame.transform.scale(self.image_r, (TILESIZE, TILESIZE))
        self.image = self.original_image
        self.rect.x = x
        self.rect.y = y

    def update(self):
        super().update()



class Enemy(Character):
    def __init__(self, all_sprites, enemy_sprites, player, x,y, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.groups = all_sprites, enemy_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.original_image = pygame.image.load("img/enemies/zoimbie1_hold.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (TILESIZE, TILESIZE))
        self.image = self.original_image
        self.x = x
        self.y = y
        self.rot = 0
        self.player = player

    def update(self):
        super().update()
        self.rot = (vec(self.player.x, self.player.y) - vec(self.x, self.y)).angle_to(vec(1,0))
        self.image = pygame.transform.rotate(self.original_image, self.rot)

