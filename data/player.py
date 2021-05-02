from settings import *
from pygame.math import Vector2 as Vec
import random as rnd


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, walls, hp=100, color=RED):
        self.life = hp
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect(x=x*TILESIZE, y=y*TILESIZE)
        self.x, self.y = x, y
        self.walls = walls

    def update(self):
        self.x = self.rect.x // TILESIZE
        self.y = self.rect.y // TILESIZE

    def check_move(self, dx, dy):
        for wall in self.walls:
            # print(self.rect.x, self.rect.y, brick.rect.x, brick.rect.y, brick.rect.w, brick.rect.h)
            # TODO tirar TILESIZE abaixo para playerwidth
            if self.has_collide(wall):
                if dx == 1:
                    self.rect.x = wall.rect.x - TILESIZE
                if dx == -1:
                    self.rect.x = wall.rect.x + wall.rect.w
                if dy == 1:
                    self.rect.y = wall.rect.y - 2 * TILESIZE
                if dy == -1:
                    self.rect.y = wall.rect.y + wall.rect.h
                self.stop()

    def has_collide(self, wall):
        px, py = self.rect.x, self.rect.y
        wx ,wy, wh, ww = wall.rect.x, wall.rect.y, wall.rect.h, wall.rect.w
        collide_hor = wx + ww > px > wx - TILESIZE
        collide_ver = wy + wh > py > wy - 2 * TILESIZE
        return collide_hor and collide_ver

    def stop(self):
        pass


class Player(Character):
    def __init__(self, x, y, walls, *args, **kwargs):
        super().__init__(x, y, walls, *args, **kwargs)
        self.front = "down"
        self.current_player_frame = 1
        self.image = pygame.image.load("img/player/p_down_1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILESIZE, 2 * TILESIZE))
        self.frames = [[]]
        self.down_image = pygame.image.load("img/player/p_down_1.png").convert_alpha()
        self.up_image = pygame.image.load("img/player/p_up_1.png").convert_alpha()
        self.left_image = pygame.image.load("img/player/p_left_1.png").convert_alpha()
        self.right_image = pygame.image.load("img/player/p_right_1.png").convert_alpha()
        self.tick = 1
        self.tick_max = 10
        self.itens = [9, 9, 9, 9, 9, 9, 9, 9, 9, 0]

        # self.original_image = pygame.transform.scale(self.original_image, (TILESIZE, TILESIZE))

    def move(self, sinalx, sinaly):
        self.rect.x += sinalx * PLAYER_SPEED
        self.rect.y += sinaly * PLAYER_SPEED
        self.tick += 1
        if self.tick > self.tick_max:
            self.tick = 1
            self.current_player_frame = self.current_player_frame % 4+1
        if sinalx == 1:
            self.image = pygame.image.load(f'img/player/p_right_{self.current_player_frame}.png').convert_alpha()
            self.front = "right"
        elif sinalx == -1:
            self.image = pygame.image.load(f'img/player/p_left_{self.current_player_frame}.png').convert_alpha()
            self.front = "left"
        elif sinaly == -1:
            self.image = pygame.image.load(f'img/player/p_up_{self.current_player_frame}.png').convert_alpha()
            self.front = "up"
        elif sinaly == 1:
            self.image = pygame.image.load(f'img/player/p_down_{self.current_player_frame}.png').convert_alpha()
            self.front = "down"
        self.check_move(sinalx, sinaly)
        self.image = pygame.transform.scale(self.image, (TILESIZE, 2*TILESIZE))

    def stop(self):
        if self.front == "down":
            self.image = self.down_image
        elif self.front == "up":
            self.image = self.up_image
        elif self.front == "left":
            self.image = self.left_image
        elif self.front == "right":
            self.image = self.right_image
        self.image = pygame.transform.scale(self.image, (TILESIZE, 2 * TILESIZE))
        self.tick = 5

    # TODO
    # def load_frames(self):



class Enemy(Character):
    def __init__(self, walls, all_sprites, enemy_sprites, player, x, y, level, *args, **kwargs):
        super().__init__(x, y, walls, *args, **kwargs)
        self.groups = all_sprites, enemy_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.original_image = pygame.image.load("img/enemies/zoimbie1_hold.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (TILESIZE, TILESIZE))
        self.image = self.original_image
        self.player = player
        self.tick = 0
        self.tmax = rnd.randrange(20, 50)
        self.furious = True
        self.level = level
        self.front = 'up'
        self.vx, self.vy = 0,0

    def update(self):
        if self.furious:
            self.target_velocity()
        else:
            self.random_velocity()

        self.walk()
        super().update()

    def target_velocity(self):
        displacement = Vec(self.player.x, self.player.y) - Vec(self.x, self.y)
        if displacement.length() != 0:
            angle = displacement.angle_to(Vec(1,0))
            print(angle)
            self.update_velocity(angle)

    def update_velocity(self, angle):
        self.vx, self.vy = 0, 0
        if 135 >= angle >= 45:
            self.vy = -1
        elif 45 >= angle >= -45:
            self.vx = 1
        elif -45 >= angle >= -135:
            self.vy = 1
        else:
            self.vx = -1
        self.update_front()

    def random_velocity(self):
        self.tick += 1
        if self.tick > self.tmax:
            self.tick = 0
            self.tmax = rnd.randrange(20, 50)
            angle = rnd.randrange(0, 360)
            self.update_velocity(angle)

    def walk(self):
        self.rect.x += ENEMY_SPEED * self.vx
        self.rect.y += ENEMY_SPEED * self.vy
        self.check_move(self.vx, self.vy)

    def update_front(self):
        if self.vx == 1:
            self.front = 'right'
        elif self.vx == -1:
            self.front = 'left'
        elif self.vy == -1:
            self.front = 'up'
        elif self.vy == 1:
            self.front = 'down'
