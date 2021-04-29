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
        self.original_image = pygame.image.load("img/player/player.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (TILESIZE, TILESIZE))
        self.image_r = pygame.image.load("img/player/player_right.png").convert_alpha()
        self.image_r = pygame.transform.scale(self.image_r, (TILESIZE, TILESIZE))
        self.image = self.original_image

    def move(self, sinalx, sinaly, walls):
        self.rect.x += sinalx * PLAYER_SPEED
        self.rect.y += sinaly * PLAYER_SPEED
        if sinalx == 1:
            self.image = self.image_r
        elif sinalx == -1:
            self.image = self.original_image
        self.check_move(walls, sinalx, sinaly)

    def check_move(self, walls, dx, dy):
        print(walls)
        for brick in walls:
            if abs(self.rect.x - brick.x * TILESIZE) < TILESIZE and abs(self.rect.y - brick.y * TILESIZE) < TILESIZE:
                if dx != 0:
                    self.rect.x = (brick.x - dx) * TILESIZE
                if dy != 0:
                    self.rect.y = (brick.y - dy) * TILESIZE


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
