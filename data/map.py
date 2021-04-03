import pygame
from settings import *

all_sprites = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.rect.x = self.x*TILESIZE;
        self.rect.y = self.y*TILESIZE;
    def horizontal(self, sinal):
        self.x += sinal;
    def vertical(self, sinal):
        self.y += sinal;

class Map:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500,50)
        
    def run(self):
        player = Player(0,0)
        self.done = False
        while not self.done:
            self.clock.tick(FPS)
            self.event()
            self.draw()

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        all_sprites.draw(self.screen)
        pygame.display.flip()
    
    def draw_grid(self):
        for y_offset in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0,y_offset), (WIDTH, y_offset))
        for x_offset in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x_offset, 0), (x_offset, WIDTH))

    def quit(self):
        pygame.quit()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
                print("saiu")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.horizontal(1)
                    print("direita")
                elif event.key == pygame.K_LEFT:
                    player.horizontal(-1)
                    print("esquerda")
                elif event.key == pygame.K_UP:
                    player.vertical(-1)
                    print("up")
                elif event.key == pygame.K_DOWN:
                    player.vertical(1)
                    print("down")
            
        all_sprites.update()


player = Player(1,1)
all_sprites.add(player)

map = Map()

map.run()
map.quit()