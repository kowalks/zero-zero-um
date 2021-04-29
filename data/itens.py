import pygame
from settings import *


class Item(pygame.sprite.Sprite):

    def __init__(self, x=0, y = 0, got = False, COLOR = LIGHTGREY):
        self.got = got
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(COLOR)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def check_got(self, player):
      if self.x == player.x and self.y == player.y:
        self.got = True

    def update(self):
        self.rect.x = self.x*TILESIZE
        self.rect.y = self.y*TILESIZE


class KeyItem(Item):
    def __init__(self, all_sprites, item_sprites, player, x, y, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.groups = all_sprites, item_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.player = player

    def check_got(self, player):
        super().check_got(player)

    def update(self):
        super().update()


class BasicAttackItem(Item):
    def __init__(self, all_sprites, item_sprites, player, x, y, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.groups = all_sprites, item_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.attack_points = 40
        self.player = player

    def check_got(self, player):
        super().check_got(player)

    def update(self):
        super().update()

  
class AdvancedAttackItem(Item):
    def __init__(self, all_sprites, item_sprites, player, x, y, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.groups = all_sprites, item_sprites
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
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.heal_points = 60
        self.player = player

    def check_got(self, player):
        super().check_got(player)

    def update(self):
        super().update()
