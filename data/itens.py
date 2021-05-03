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

    def show_key_password(self, screen, password):
        keySurface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        keySurface.set_alpha(128)  # alpha level
        keySurface.fill(BLACK)  # this fills the entire surface
        keyRect = keySurface.get_rect()
        screen.blit(keySurface, keyRect)
        smallfont = pygame.font.Font(f'fonts/{BT_FONT}.ttf', 22)

        message_l1 = f"Uma aeronave AT-{password.airplane_n}, saindo da base aérea de UET, às {password.departure_time}h"
        message_l2 = f"de Zulu carregando {password.sigsauer_rifles} fuzis SigSauer e {password.atomic_bombs} bombas atômicas"
        message_l3 = f"e {password.lmg_rifles} metralhadoras .{password.lmg_caliber} devendo chegar às {password.arrival_time}h em Zulu"

        full_message = [message_l1, message_l2, message_l3]

        surfaces_list = []
        linespace = 30
        line_number = 0
        for line in full_message:
            text_surface = smallfont.render(line, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.center = (
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + (line_number - 1) * linespace)
            line_number += 1
            s = (text_surface, text_rect)
            surfaces_list.append(s)
        for s in surfaces_list:
            screen.blit(*s)



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


class HealItem(Item):
    def __init__(self, all_sprites, heal_sprites, player, x, y, *args, **kwargs):
        super().__init__(x, y, *args, **kwargs)
        self.groups = all_sprites, heal_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.original_image = pygame.image.load("img/enemies/zoimbie1_hold.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (TILESIZE, TILESIZE))
        self.image = self.original_image
        self.player = player
        self.x = x
        self.y = y

    def update(self):
        super().update()


class AttackItem(Item):
    def __init__(self, all_sprites, attack_sprites, player, x, y, *args, **kwargs):
        super().__init__(x, y, *args, **kwargs)
        self.groups = all_sprites, attack_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.original_image = pygame.image.load("img/enemies/zoimbie1_hold.png").convert_alpha()
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
        self.original_image = pygame.image.load("img/enemies/zoimbie1_hold.png").convert_alpha()
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
        self.original_image = pygame.image.load("img/enemies/zoimbie1_hold.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (TILESIZE, TILESIZE))
        self.image = self.original_image
        self.player = player
        self.x = x
        self.y = y

    def update(self):
        super().update()


class AdvancedHealItem(Item):
    def __init__(self, all_sprites, advance_heal_sprites, player, x, y, *args, **kwargs):
        super().__init__(x, y, *args, **kwargs)
        self.groups = all_sprites, advance_heal_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.original_image = pygame.image.load("img/enemies/zoimbie1_hold.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (TILESIZE, TILESIZE))
        self.image = self.original_image
        self.player = player
        self.x = x
        self.y = y

    def update(self):
        super().update()


class ImproveAttackItem(Item):
    def __init__(self, all_sprites, improve_attack_sprites, player, x, y, *args, **kwargs):
        super().__init__(x, y, *args, **kwargs)
        self.groups = all_sprites, improve_attack_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.original_image = pygame.image.load("img/enemies/zoimbie1_hold.png").convert_alpha()
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


