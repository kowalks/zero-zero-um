import pygame
from settings import *
import player
from wall import *
from room import *
import buttons


class Map:
    def __init__(self, screen):
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500,50)
        self.my_player = player.Player(5, 5)
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.all_sprites.add(self.my_player)
        self.map_image = self.set_rooms()
        self.map_image = pygame.transform.scale(self.map_image, (MAPSIZE*ROOMSIZE*TILESIZE,MAPSIZE*ROOMSIZE*TILESIZE))
        self.map_rect = self.map_image.get_rect()
        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.enemies = pygame.sprite.Group()
        self.my_enemy = player.Enemy(self.all_sprites, self.enemies, self.my_player, 1,1,41)
        self.my_enemy = player.Enemy(self.all_sprites, self.enemies, self.my_player, 5, 6,54)
        self.my_enemy = player.Enemy(self.all_sprites, self.enemies, self.my_player, 7, 7,545)
        self.my_enemy = player.Enemy(self.all_sprites, self.enemies, self.my_player, 7, 8, 13)
        self.my_enemy = player.Enemy(self.all_sprites, self.enemies, self.my_player, 10, 7,2)
        self.my_enemy = player.Enemy(self.all_sprites, self.enemies, self.my_player, 7, 11,899)
        self.dt = 0

    def set_rooms(self):
        all_room_img = pygame.Surface((MAPSIZE*ROOMSIZE*ROOMSIZE, MAPSIZE*ROOMSIZE*ROOMSIZE))
        room_list = [[TiledRoom("up_left_corner"),TiledRoom("up_middle_corner"),TiledRoom("up_middle_corner"),TiledRoom("up_middle_corner"),TiledRoom("up_middle_corner")]]
        for col in range(MAPSIZE):
            all_room_img = room_list[0][col].make_room(all_room_img, col, 0)

        return all_room_img

    def run(self, screen, running):
        while running:
            self.dt = self.clock.tick(FPS)/1000
            running = self.event(running)
            self.draw(screen)

    def draw(self, screen):
        screen.fill(BLACK)
        # self.draw_grid(screen)

        screen.blit(self.map_image, self.camera.apply_rect(self.map_rect))

        for sprite in self.all_sprites:
            screen.blit(sprite.image, self.camera.apply(sprite))
        self.draw_info(screen)
        self.check_collision(screen)
        pygame.display.flip()

    def draw_grid(self, screen):
        for y_offset in range(0, SCREEN_HEIGHT, TILESIZE):
            pygame.draw.line(screen, LIGHTGREY, (0,y_offset), (SCREEN_WIDTH, y_offset))
        for x_offset in range(0, SCREEN_WIDTH, TILESIZE):
            pygame.draw.line(screen, LIGHTGREY, (x_offset, 0), (x_offset, SCREEN_WIDTH))

    def event(self, running):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.my_player.move(1,0, self.walls)
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.my_player.move(-1,0, self.walls)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.my_player.move(0,-1, self.walls)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.my_player.move(0,1, self.walls)
        elif keys[pygame.QUIT]:
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        self.all_sprites.update()
        self.camera.update(self.my_player)
        # pygame.sprite.spritecollide(self.my_player, self.enemies, 1)
        return running

    def check_collision(self, screen):
        for enemy in self.enemies:
            if abs(self.my_player.rect.x - enemy.rect.x) < TILESIZE and abs(self.my_player.rect.y - enemy.rect.y) < TILESIZE:
                while enemy.life > 0 and self.my_player.life > 0:
                    pop_up(self.my_player, enemy, screen)
                if enemy.life <= 0:
                    enemy.kill()
                break




    def draw_info(self, screen):
        font = pygame.font.Font(f'fonts/{BT_FONT}.ttf', 30)

        # Players Life
        pl_life_text = font.render('Vida:', True, WHITE)
        vida_text = pl_life_text.get_rect(bottomleft=(TILESIZE/2, TILESIZE))

        pl_life = font.render(str(self.my_player.life), True, RED)
        vida = pl_life.get_rect(bottomleft=(vida_text.right, TILESIZE))

        lifeSurface = pygame.Surface(((vida.width + vida_text.width)*1.2, vida.height*1.2))  # the size of your rect
        lifeSurface.set_alpha(128)  # alpha level
        lifeSurface.fill(BLACK)  # this fills the entire surface
        rect = lifeSurface.get_rect()
        rect.left = vida_text.left - 0.1*((vida.width + vida_text.width))
        rect.y = vida_text.y - 0.1*vida.height
        screen.blit(lifeSurface, rect)
        screen.blit(pl_life_text, vida_text)
        screen.blit(pl_life, vida)



class Camera:
    def __init__(self, sizeX, sizeY):
        self.camera = pygame.Rect(0,0,sizeX, sizeY)
        self.width= sizeX
        self.height = sizeY

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)  # New Rect moved

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    def update(self, player):
        # To center: (SCREEN_WIDTH/2) and (SCREEN_HEIGHT/2)
        x = -player.rect.x + (SCREEN_WIDTH/2)
        y = -player.rect.y + (SCREEN_HEIGHT/2)
        self.camera = pygame.Rect(x, y, self.width, self.height)


def pop_up(player, enemy, screen):
        BLUE = GREEN
        screen.fill(BGCOLOR)
        font = pygame.font.Font(f'fonts/{BT_FONT}.ttf', 30)
        # Title
        img = font.render('Combate', True, WHITE)
        rect = img.get_rect(center = (SCREEN_WIDTH/2, TILESIZE))
        screen.blit(img, rect)

        # Players Life
        pl_life = font.render('Vida:', True, WHITE)
        vida =pl_life.get_rect(bottomleft = (TILESIZE, 3*TILESIZE))
        screen.blit(pl_life, vida)

        jogador = font.render("Jogador", True, WHITE)
        player_title = jogador.get_rect(bottomleft=(TILESIZE, vida.top))
        screen.blit(jogador, player_title)

        pl_life = font.render(str(player.life), True, RED)
        vida = pl_life.get_rect(bottomleft=(vida.right, 3 * TILESIZE))
        screen.blit(pl_life, vida)

        # Enemy Life
        jogador = font.render("Inimigo", True, WHITE)
        enemy_title = jogador.get_rect(bottomright=(SCREEN_WIDTH - TILESIZE, vida.top))
        screen.blit(jogador, enemy_title)

        pl_life = font.render('Vida:', True, WHITE)
        vida = pl_life.get_rect(bottomleft = (enemy_title.left, 3*TILESIZE))
        screen.blit(pl_life, vida)

        pl_life = font.render(str(enemy.life), True, RED)
        vida = pl_life.get_rect(bottomleft=(vida.right, 3 * TILESIZE))
        screen.blit(pl_life, vida)

        BACK = (70, 70, 70)
        #Rect for actions
        rect = pygame.Rect(50, 60, SCREEN_WIDTH-2*TILESIZE, 0.4*SCREEN_HEIGHT)
        rect.midbottom = (SCREEN_WIDTH/2, SCREEN_HEIGHT - TILESIZE/4)
        pygame.draw.rect(screen, BACK, rect, border_radius=10)

        #Buttons
        atck1 = buttons.ButtonFight(rect.x + (rect.right - rect.left)/4,
                                   rect.y + TILESIZE/2,
                                   "Atacar", "withe_button")
        atck1.draw_button(screen)

        atck = buttons.ButtonFight(rect.x + (rect.right - rect.left)/4,
                                   rect.y + TILESIZE/2 + 2*TILESIZE,
                                   "Atacar", "withe_button")
        atck.draw_button(screen)

        itens = font.render("Itens", True, WHITE)
        itenspos = itens.get_rect(midtop = (rect.center[0] + (rect.right - rect.left)/4, rect.y  + TILESIZE/4))
        screen.blit(itens, itenspos)

        #ITENS
        nTILESIZE = 1.2*TILESIZE
        rect_itens = pygame.Rect(0,0, nTILESIZE, nTILESIZE)


        for y_off in range(0, 3, 1):
            for x_off in range(0, 3,1):
                rect_itens.topleft = (itenspos.bottomleft[0] + x_off*nTILESIZE,itenspos.bottomleft[1]+y_off*nTILESIZE)
                pygame.draw.rect(screen, (50, 50, 50), rect_itens)
                pygame.draw.rect(screen, WHITE, rect_itens, width=1)

       #mouse position
        mx, my = pygame.mouse.get_pos()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if click:
            if atck1.rectangle.collidepoint((mx, my)):
                enemy.life-=1
            if atck.rectangle.collidepoint((mx, my)):
                enemy.life -= 50
        pygame.display.flip()