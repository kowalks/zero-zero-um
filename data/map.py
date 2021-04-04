import pygame
from settings import *
import player
from wall import *
from room import *


class Map:
    def __init__(self, screen):
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500,50)
        self.my_player = player.Player(5, 5)
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.all_sprites.add(self.my_player)
        self.set_rooms()
        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.enemies = pygame.sprite.Group()
        self.my_enemy = player.Enemy(self.all_sprites, self.enemies, self.my_player, 1,1)
        self.my_enemy = player.Enemy(self.all_sprites, self.enemies, self.my_player, 5, 6)
        self.my_enemy = player.Enemy(self.all_sprites, self.enemies, self.my_player, 7, 7)
        self.my_enemy = player.Enemy(self.all_sprites, self.enemies, self.my_player, 7, 8)
        self.my_enemy = player.Enemy(self.all_sprites, self.enemies, self.my_player, 10, 7)
        self.my_enemy = player.Enemy(self.all_sprites, self.enemies, self.my_player, 7, 11)


    def set_rooms(self):
        room1 = Room("room1")
        for row in range(MAPSIZE):
            for col in range(MAPSIZE):
                room1.generate_walls(self.all_sprites, self.walls,
                                     col*ROOMSIZE, row*ROOMSIZE)

    def run(self, screen, running):
        self.done = False
        while not self.done:
            self.clock.tick(FPS)
            self.event(running)
            self.draw(screen)

    def draw(self, screen):
        screen.fill(BGCOLOR)
        # self.draw_grid(screen)
        for sprite in self.all_sprites:
            screen.blit(sprite.image, self.camera.apply(sprite))
        pygame.display.flip()
    
    def draw_grid(self, screen):
        for y_offset in range(0, SCREEN_HEIGHT, TILESIZE):
            pygame.draw.line(screen, LIGHTGREY, (0,y_offset), (SCREEN_WIDTH, y_offset))
        for x_offset in range(0, SCREEN_WIDTH, TILESIZE):
            pygame.draw.line(screen, LIGHTGREY, (x_offset, 0), (x_offset, SCREEN_WIDTH))

    def event(self, running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.my_player.move(1,0, self.walls)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.my_player.move(-1,0, self.walls)
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.my_player.move(0,-1, self.walls)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.my_player.move(0,1, self.walls)

        self.all_sprites.update()
        self.camera.update(self.my_player)
        # pygame.sprite.spritecollide(self.my_player, self.enemies, 1)
        return running


class Camera:
    def __init__(self, sizeX, sizeY):
        self.camera = pygame.Rect(0,0,sizeX, sizeY)
        self.width= sizeX
        self.height = sizeY

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft); #New Rect moved

    def update(self, player):
        # To center: (SCREEN_WIDTH/2) and (SCREEN_HEIGHT/2)
        x = -player.rect.x + (SCREEN_WIDTH/2)
        y = -player.rect.y + (SCREEN_HEIGHT/2)
        self.camera = pygame.Rect(x, y, self.width, self.height)