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
    
    def set_rooms(self):
        room1 = Room("room1")
        room1.generate_walls(self.all_sprites, self.walls)
          
    def run(self, screen, running):
        self.done = False
        while not self.done:
            self.clock.tick(FPS)
            self.event(running)
            self.draw(screen)

    def draw(self, screen):
        screen.fill(BGCOLOR)
        self.draw_grid(screen)
        self.all_sprites.draw(screen)
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
                if event.key == pygame.K_RIGHT:
                    self.my_player.move(1,0, self.walls)
                elif event.key == pygame.K_LEFT:
                    self.my_player.move(-1,0, self.walls)
                elif event.key == pygame.K_UP:
                    self.my_player.move(0,-1, self.walls)
                elif event.key == pygame.K_DOWN:
                    self.my_player.move(0,1, self.walls)

        self.all_sprites.update()
        return running


