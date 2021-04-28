import pygame
from settings import *


class Item(pygame.sprite.Sprite, *args, **kwargs):
    def __init__(self, x=0, y=0, got=False, COLOR=LIGHTGREY, *args, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(COLOR)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.got = got

    """Detecta se o jogador pegou o item"""

    def check_got(self, player):
        if (self.x == player.x and self.y == player.y):
            self.got = True

    def update(self):
        if (self.got)
            """remover item da tela e adicionar ao player"""
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


"""Iteração com jogador: atributo getout"""


class Key_item(Item):
    def __init__(self, *args, **kwargs):
        super().__init(*args, **kwargs)

    def check_got(self, player):
        if (self.x == player.x and self.y == player.y):
            self.got = True
            player.getout = True


class basic_attack_item(Item):
    def __init__(self, *args, **kwargs):
        super().__init(*args, **kwargs)
        self.attack_points = 40


class advanced_attack_item(Item):
    def __init__(self, *args, **kwargs):
        super().__init(*args, **kwargs)
        self.attack_points = 80


class basic_heal_item(Item):
    def __init__(self, *args, **kwargs):
        super().__init(*args, **kwargs)
        self.heal_points = 30


class advanced_heal_item(Item):
    def __init__(self, *args, **kwargs):
        super().__init(*args, **kwargs)
        self.heal_points = 60

