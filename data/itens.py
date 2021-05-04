import pygame
from settings import *
import screens as scn
class Item(pygame.sprite.Sprite):

    def __init__(self, x, y, got=False, COLOR=LIGHTGREY):
        self.got = got
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.x = x
        self.y = y

    def update(self):
        self.rect.x = self.x*TILESIZE
        self.rect.y = self.y*TILESIZE


class KeyItem(Item):
    def __init__(self, all_sprites, key_sprites, player, x, y, *args, **kwargs):
        super().__init__(x, y, *args, **kwargs)
        self.groups = all_sprites, key_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load("img/itens/message.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.player = player


class ClockItem(Item):
    def __init__(self, all_sprites, clock_sprites, player, x, y, *args, **kwargs):
        super().__init__(x, y, *args, **kwargs)
        self.groups = all_sprites, clock_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.original_image = pygame.image.load("img/itens/ice_clock.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (TILESIZE, TILESIZE))
        self.image = self.original_image
        self.player = player
        self.x = x
        self.y = y

    def update(self):
        super().update()


class SupremeItem(Item):
    def __init__(self, all_sprites, supreme_sprites, player, x, y, *args, **kwargs):
        super().__init__(x, y, *args, **kwargs)
        self.groups = all_sprites, supreme_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.original_image = pygame.image.load("img/itens/fish.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (TILESIZE, TILESIZE))
        self.image = self.original_image
        self.player = player
        self.x = x
        self.y = y

    def update(self):
        super().update()


class DefenceItem(Item):
    def __init__(self, all_sprites, defence_sprites, player, x, y, *args, **kwargs):
        super().__init__(x, y, *args, **kwargs)
        self.groups = all_sprites, defence_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.original_image = pygame.image.load("img/itens/vest.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (TILESIZE, TILESIZE))
        self.image = self.original_image
        self.player = player
        self.x = x
        self.y = y

    def update(self):
        super().update()


class AdvancedAttackItem(Item):
    def __init__(self, all_sprites, advance_attack_sprites, player, x, y, *args, **kwargs):
        super().__init__(x, y, *args, **kwargs)
        self.groups = all_sprites, advance_attack_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.original_image = pygame.image.load("img/itens/boot.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (TILESIZE, TILESIZE))
        self.image = self.original_image
        self.player = player
        self.x = x
        self.y = y

    def update(self):
        super().update()


class ImproveLifeItem(Item):
    def __init__(self, all_sprites, improve_life_sprites, player, x, y, *args, **kwargs):
        super().__init__(x, y, *args, **kwargs)
        self.groups = all_sprites, improve_life_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.original_image = pygame.image.load("img/itens/canteen.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (TILESIZE, TILESIZE))
        self.image = self.original_image
        self.player = player
        self.x = x
        self.y = y

    def update(self):
        super().update()

class EndGameItem(Item):
    def __init__(self, all_sprites, end_game_sprites, player, x, y, *args, **kwargs):
        super().__init__(x, y, *args, **kwargs)
        self.groups = all_sprites, end_game_sprites
        self.image = pygame.Surface((1, 1))
        self.image.fill(BGCOLOR)
        pygame.sprite.Sprite.__init__(self, self.groups)
        # self.original_image = pygame.image.load("img/itens/invisivel.png").convert_alpha()
        self.player = player
        self.x = x
        self.y = y

    def update(self):
        super().update()


