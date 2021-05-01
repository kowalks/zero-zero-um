from settings import *
from pygame.math import Vector2 as Vec
import random as rnd


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, walls, hp=100, color=RED):
        self.life = hp
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
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


class Player(Character):
    def __init__(self, x, y,walls ,*args, **kwargs):
        super().__init__(x, y,walls, *args, **kwargs)
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

        # self.original_image = pygame.transform.scale(self.original_image, (TILESIZE, TILESIZE))

    def move(self, sinalx, sinaly):
        self.rect.x += sinalx * PLAYER_SPEED
        self.rect.y += sinaly * PLAYER_SPEED
        self.tick+=1
        if self.tick > self.tick_max:
            self.tick = 1
            self.current_player_frame = self.current_player_frame%4+1
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
        self.image = pygame.transform.scale(self.image,
                                            (TILESIZE, 2 * TILESIZE))
        self.tick=5
    def check_move(self, dx, dy):
        for brick in self.walls:
            print(self.rect.x, self.rect.y, brick.rect.x, brick.rect.y, brick.rect.w, brick.rect.h)
            # TODO tirar TILESIZE abaixo para playerwidth
            if self.rect.x < brick.rect.x + brick.rect.w and self.rect.x > brick.rect.x - TILESIZE and \
                    self.rect.y < brick.rect.y + brick.rect.h and self.rect.y > brick.rect.y - 2 * TILESIZE:
                print("Colidiu")
                if dx == 1:
                    self.rect.x = brick.rect.x - TILESIZE
                if dx == -1:
                    self.rect.x = brick.rect.x + brick.rect.w
                if dy == 1:
                    self.rect.y = brick.rect.y - 2 * TILESIZE
                if dy == -1:
                    self.rect.y = brick.rect.y + brick.rect.h




    # TODO
    # def load_frames(self):



class Enemy(Character):
    def __init__(self, walls, all_sprites, enemy_sprites, player, x, y, *args, **kwargs):
        super().__init__(x, y,walls, *args, **kwargs)
        self.groups = all_sprites, enemy_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.original_image = pygame.image.load("img/enemies/zoimbie1_hold.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (TILESIZE, TILESIZE))
        self.image = self.original_image
        self.player = player
        self.velocity = Vec(1, 0).rotate(rnd.randrange(0, 360))
        self.tmax = rnd.randrange(20, 50)
        self.tick = 0
        self.furious = rnd.randint(0, 1)

    def update(self):
        # self.rot = (vec(self.player.x, self.player.y) - vec(self.x, self.y)).angle_to(vec(1,0))
        if self.furious:
            self.target_velocity()
        else:
            self.random_velocity()

        self.walk()
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
            print(self.rect.x, self.rect.y, brick.rect.x, brick.rect.y, brick.rect.w, brick.rect.h)
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



