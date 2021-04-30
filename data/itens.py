import pygame
from settings import *
import random as rnd #teste, apagar depois
from pygame.math import Vector2 as Vec  #teste, apagar depois


class Item(pygame.sprite.Sprite):

    def __init__(self, x, y, got = False, COLOR = LIGHTGREY):
        self.got = got
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.x = x
        self.y = y


    def check_got(self, player):
        if self.x == player.x and self.y == player.y:
            self.got = True
        return self.got


    def update(self):
        self.rect.x = self.x*TILESIZE // TILESIZE
        self.rect.y = self.y*TILESIZE // TILESIZE


class KeyItem(Item):
    def __init__(self, player, x, y, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = x
        self.y = y
        self.player = player
        self.COLOR = GREEN


    def check_got(self, player):
        super().check_got(player)

    def update(self):
        super().update()


class ClockItem(Item):
    def __init__(self, all_sprites, clock_sprites, player, x, y, *args, **kwargs):
        super().__init__(x, y, *args, **kwargs)
        self.groups = all_sprites, clock_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.original_image = pygame.image.load("img/enemies/zoimbie1_hold.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (TILESIZE, TILESIZE))
        self.image = self.original_image
        self.player = player
        self.x = x
        self.y = y

    def update(self):
        super().update()

    def check_got(self, player):
        super().check_got(player)

  
class AdvancedAttackItem(Item):
    def __init__(self, all_sprites, item_sprites, player, x, y, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.groups = all_sprites, item_sprites
        while check_got(player):
            pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.attack_points = 80
        self.player = player

    def check_got(self, player):
        super().check_got(player)

    def update(self):
        super().update()

class BasicHealItem(Item):
    def __init__(self, all_sprites, item_sprites, player, x, y, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.groups = all_sprites, item_sprites
        while check_got(player):
            pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.heal_points = 30
        self.player = player

    def check_got(self, player):
        super().check_got(player)

    def update(self):
        super().update()


class AdvancedHealItem(Item):
    def __init__(self, all_sprites, item_sprites, player, x, y, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.groups = all_sprites, item_sprites
        while check_got(player):
            pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.heal_points = 60
        self.player = player

    def check_got(self, player):
        super().check_got(player)

    def update(self):
        super().update()
