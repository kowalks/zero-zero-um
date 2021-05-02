from settings import *
from pygame.math import Vector2 as Vec
import random as rnd

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, walls, hp=100):
        self.life = hp
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.frames = {}
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.walls = walls

    def update(self):
        self.x = self.rect.x // TILESIZE
        self.y = self.rect.y // TILESIZE

    def check_move(self, dx, dy):
        pass

    def load_frames(self, type):
        frames = {}
        direction = ["down", "up", "left", "right"]
        for dir in direction:
            list = []
            for i in range(4):
                list.append(pygame.image.load(f"img/{type}/{type}_{dir}_{i+1}.png").convert_alpha())
            frames[dir] = list
        for dir in direction:
            for i in range(4):
                frames[dir][i] = pygame.transform.scale(frames[dir][i], (TILESIZE, 2*TILESIZE))
        return frames

class Player(Character):
    def __init__(self, x, y, walls, *args, **kwargs):
        super().__init__(x, y, walls, *args, **kwargs)
        self.current_player_frame = 0
        self.frames = self.load_frames("player")
        self.image = self.frames["down"][0]
        self.front = "down"
        self.tick = 1
        self.tick_max = 10
        self.itens = [9, 9, 9, 9, 9, 9, 9, 9, 9, 0]

    def move(self, sinalx, sinaly):
        self.rect.x += sinalx * PLAYER_SPEED
        self.rect.y += sinaly * PLAYER_SPEED
        self.tick += 1
        if self.tick > self.tick_max:
            self.tick = 1
            self.current_player_frame = (self.current_player_frame+1) % 4
        if sinalx == 1:
            self.image = self.frames["right"][self.current_player_frame]
            self.front = "right"
        elif sinalx == -1:
            self.image = self.frames["left"][self.current_player_frame]
            self.front = "left"
        elif sinaly == -1:
            self.image = self.frames["up"][self.current_player_frame]
            self.front = "up"
        elif sinaly == 1:
            self.image = self.frames["down"][self.current_player_frame]
            self.front = "down"
        self.check_move(sinalx, sinaly)

    def stop(self):
        self.image = self.frames[self.front][0]
        self.tick = 5

    def check_move(self, dx, dy):
        for brick in self.walls:
            # print(self.rect.x, self.rect.y, brick.rect.x, brick.rect.y, brick.rect.w, brick.rect.h)
            # TODO tirar TILESIZE abaixo para playerwidth
            if self.rect.x < brick.rect.x + brick.rect.w and self.rect.x > brick.rect.x - TILESIZE and \
                    self.rect.y < brick.rect.y + brick.rect.h and self.rect.y > brick.rect.y - 2*TILESIZE:
                if dx == 1:
                    self.rect.x = brick.rect.x - TILESIZE
                    self.stop()
                if dx == -1:
                    self.rect.x = brick.rect.x + brick.rect.w
                    self.stop()
                if dy == 1:
                    self.rect.y = brick.rect.y - 2*TILESIZE
                    self.stop()
                if dy == -1:
                    self.rect.y = brick.rect.y + brick.rect.h
                    self.stop()


class Enemy(Character):
    def __init__(self, walls, all_sprites, enemy_sprites, player, x, y, level, *args, **kwargs):
        super().__init__(x, y, walls, *args, **kwargs)
        self.groups = all_sprites, enemy_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.frames = self.load_frames("enemies") # todos frames ja loadados
        self.original_image = pygame.image.load("img/enemies/zoimbie1_hold.png").convert_alpha() # tirar depois
        self.original_image = pygame.transform.scale(self.original_image, (TILESIZE, TILESIZE))
        self.image = self.original_image
        self.player = player
        self.velocity = Vec(1, 0).rotate(rnd.randrange(0, 360))
        self.tick = 0
        self.tmax = rnd.randrange(20, 50)
        self.furious = rnd.randint(0, 1)
        self.level = level

    def update(self):
        # self.rot = (vec(self.player.x, self.player.y) - vec(self.x, self.y)).angle_to(vec(1,0))
        if self.furious:
            self.target_velocity()
        else:
            self.random_velocity()

        # self.walk()
        phi = self.velocity.angle_to(Vec(1, 0))
        self.image = pygame.transform.rotate(self.original_image, phi)
        super().update()

    def target_velocity(self):
        displacement = Vec(self.player.x, self.player.y) - Vec(self.x, self.y)
        if displacement.length() == 0:
            self.velocity = Vec(0, 0)
        else:
            self.velocity = displacement.normalize()

    def random_velocity(self):
        self.tick += 1
        if self.tick > self.tmax:
            self.tick = 0
            self.tmax = rnd.randrange(20, 50)
            self.velocity = Vec(1, 0).rotate(rnd.randrange(0, 360))

    def walk(self):
        self.rect.x += ENEMY_SPEED * self.velocity.x
        self.rect.y += ENEMY_SPEED * self.velocity.y
        sinalx = 0 if self.velocity.x == 0 else int(self.velocity.x/abs(self.velocity.x))
        sinaly = 0 if self.velocity.y == 0 else int(self.velocity.y / abs(self.velocity.y))
        self.check_move(sinalx, sinaly)

    def check_move(self, dx, dy):
        for brick in self.walls:
            # print(self.rect.x, self.rect.y, brick.rect.x, brick.rect.y, brick.rect.w, brick.rect.h)
            # TODO tirar TILESIZE abaixo para playerwidth
            if self.rect.x < brick.rect.x + brick.rect.w and self.rect.x > brick.rect.x - TILESIZE and \
                    self.rect.y < brick.rect.y + brick.rect.h and self.rect.y > brick.rect.y - 2 * TILESIZE:
                print("Colidiu")
                if dx == 1:
                    self.rect.x = brick.rect.x - TILESIZE
                if dx == -1:
                    self.rect.x = brick.rect.x + brick.rect.w
                if dy == 1:
                    self.rect.y = brick.rect.y - TILESIZE
                if dy == -1:
                    self.rect.y = brick.rect.y + brick.rect.h



