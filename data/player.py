from settings import *
from pygame.math import Vector2 as Vec
import random as rnd

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, walls, hp=100):
        self.life = hp
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(x=x*TILESIZE, y=y*TILESIZE)
        self.x, self.y = x, y
        self.walls = walls

    def update(self):
        self.x = self.rect.x // TILESIZE
        self.y = self.rect.y // TILESIZE

    def check_move(self, dx, dy):
        for wall in self.walls:
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
        self.itens = [0, 0, 0, 0, 0]

    def move(self, sinalx, sinaly):
        self.rect.x += sinalx * PLAYER_SPEED
        self.rect.y += sinaly * PLAYER_SPEED
        self.tick += 1
        if self.tick > self.tick_max:
            self.tick = 1
            self.current_player_frame = (self.current_player_frame+1) % 4
        if sinalx == 1:
            self.front = "right"
        elif sinalx == -1:
            self.front = "left"
        elif sinaly == -1:
            self.front = "up"
        elif sinaly == 1:
            self.front = "down"
        self.image = self.frames[self.front][self.current_player_frame]
        self.check_move(sinalx, sinaly)

    def stop(self):
        self.image = self.frames[self.front][0]
        self.tick = 5



class Enemy(Character):
    def __init__(self, walls, all_sprites, enemy_sprites, player, x, y, level, *args, **kwargs):
        super().__init__(x, y, walls, *args, **kwargs)
        self.groups = all_sprites, enemy_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.current_enemy_frame = 0
        self.level = level
        self.frames = self.load_frames("enemies")
        self.player = player
        self.velocity = Vec(1, 0).rotate(rnd.randrange(0, 360))
        self.tick_frame = 0
        self.tick_max_frame = 10
        self.tick_walk = 0
        self.tick_max_walk = rnd.randrange(20, 50)
        self.furious = False
        self.front = "down"
        self.vx, self.vy = 0, 0


    def update(self):
        self.update_near_player()
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
        self.tick_walk += 1
        if self.tick_walk > self.tick_max_walk:
            self.tick_walk = 0
            self.tick_max_walk = rnd.randrange(20, 50)
            angle = rnd.randrange(0, 360)
            self.update_velocity(angle)

    def walk(self):
        self.rect.x += ENEMY_SPEED * self.vx
        self.rect.y += ENEMY_SPEED * self.vy
        self.render_image()
        self.check_move(self.vx, self.vy)

    def stop(self):
        self.image = self.frames[self.front][0]
        self.tick_frame = 5

    def update_front(self):
        if self.vx == 1:
            self.front = "right"
        elif self.vx == -1:
            self.front = "left"
        elif self.vy == -1:
            self.front = "up"
        elif self.vy == 1:
            self.front = "down"

    def update_near_player(self):
        displacement = Vec(self.player.x, self.player.y) - Vec(self.x, self.y)
        if displacement.length() <= 4:
            self.furious = True
        if displacement.length() >= 12:
            self.furious = False


    def render_image(self):
        self.tick_frame += 1
        if self.tick_frame > self.tick_max_frame:
            self.tick_frame = 1
            self.current_enemy_frame = (self.current_enemy_frame + 1) % 4
        self.image = self.frames[self.front][self.current_enemy_frame]

    def load_frames(self, type):
        frames = {}
        direction = ["down", "up", "left", "right"]
        for dir in direction:
            list = []
            for i in range(4):
                list.append(pygame.image.load(
                    f"img/{type}/level_{self.level}/{type}_{dir}_{i + 1}.png").convert_alpha())
            frames[dir] = list
        for dir in direction:
            for i in range(4):
                frames[dir][i] = pygame.transform.scale(frames[dir][i], (
                TILESIZE, 2 * TILESIZE))
        return frames


class BlockingEnemy(Character):
    def __init__(self, walls, all_sprites, enemy_sprites, player, x, y, *args, **kwargs):
        super().__init__(x, y, walls, *args, **kwargs)
        self.groups = all_sprites, enemy_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.player = player
        self.image = pygame.image.load(f"img/enemies/blocking_enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILESIZE, 2*TILESIZE))
