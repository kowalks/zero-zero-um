from settings import *
vec = pygame.math.Vector2


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, hp=100, COLOR=RED):
        self.life = hp
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def update(self):
        self.x = self.rect.x // TILESIZE
        self.y = self.rect.y // TILESIZE


class Player(Character):
    def __init__(self, x, y, *args, **kwargs):
        super().__init__(x, y, *args, **kwargs)
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


    def move(self, sinalx, sinaly, walls):
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
        self.check_move(walls, sinalx, sinaly)
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

    def check_move(self, walls, dx, dy):
        print(walls)
        for brick in walls:
            if abs(self.rect.x - brick.x * TILESIZE) < TILESIZE and abs(self.rect.y - brick.y * TILESIZE) < TILESIZE:
                if dx != 0:
                    self.rect.x = (brick.x - dx) * TILESIZE
                if dy != 0:
                    self.rect.y = (brick.y - dy) * TILESIZE

    # TODO
    # def load_frames(self):



class Enemy(Character):
    def __init__(self, all_sprites, enemy_sprites, player, x, y, *args, **kwargs):
        super().__init__(x, y, *args, **kwargs)
        self.groups = all_sprites, enemy_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.original_image = pygame.image.load("img/enemies/zoimbie1_hold.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (TILESIZE, TILESIZE))
        self.image = self.original_image
        self.rot = 0
        self.player = player

    def update(self):
        super().update()
        self.rot = (vec(self.player.x, self.player.y) - vec(self.x, self.y)).angle_to(vec(1,0))
        self.image = pygame.transform.rotate(self.original_image, self.rot)
