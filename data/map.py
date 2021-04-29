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


    def set_rooms(self):
        all_room_img = pygame.Surface((MAPSIZE*ROOMSIZE*ROOMSIZE, MAPSIZE*ROOMSIZE*ROOMSIZE))
        room1 = TiledRoom('room_16_teste')
        all_room_img = room1.make_room(all_room_img)

        # room_list = [[Room("up_left_corner"),Room("up_middle_corner"),Room("up_middle_corner"),Room("up_middle_corner"),Room("up_right_corner")],
        #              [Room("middle_left_corner"),Room("room3"),Room("room1"),Room("room1"),Room("middle_right_corner")],
        #              [Room("middle_left_corner"),Room("room1"),Room("room2"),Room("room1"),Room("middle_right_corner")],
        #              [Room("middle_left_corner"),Room("room4"),Room("room1"),Room("room4"),Room("middle_right_corner")],
        #              [Room("down_left_corner"), Room("down_middle_corner"), Room("down_middle_corner"), Room("down_middle_corner"),
        #               Room("down_right_corner")]
        #               ]
        # for rw in range(MAPSIZE):
        #     for col in range(MAPSIZE):
        #         room_list[rw][col].generate_walls(self.all_sprites, self.walls,
        #                              col*ROOMSIZE, rw*ROOMSIZE)
        return  all_room_img

    def run(self, screen, running):
        self.done = False
        while not self.done:
            self.clock.tick(FPS)
            self.event(running)
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


    def check_collision(self, screen):
        Collide = False
        for enemy in self.enemies:
            if (self.my_player.x == enemy.x and self.my_player.y == enemy.y):
                enemy_battle = enemy;
                Collide = True
                break;

        if Collide == True:
            pop_up(self.my_player, enemy_battle, screen);

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
        return entity.rect.move(self.camera.topleft); #New Rect moved

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
    #Title
    img = font.render('Combate', True, WHITE)
    rect = img.get_rect(center = (SCREEN_WIDTH/2, TILESIZE))
    screen.blit(img, rect)

    #Players Life
    pl_life = font.render('Vida:', True, WHITE)
    vida =pl_life.get_rect(bottomleft = (TILESIZE, 3*TILESIZE))
    screen.blit(pl_life, vida)

    jogador = font.render("Jogador", True, WHITE)
    player_title = jogador.get_rect(bottomleft=(TILESIZE, vida.top))
    screen.blit(jogador, player_title)

    pl_life = font.render(str(player.life), True, RED)
    vida = pl_life.get_rect(bottomleft=(vida.right, 3 * TILESIZE))
    screen.blit(pl_life, vida)

    #Enemy Life
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
    ng_button = buttons.ButtonFight(rect.x + (rect.right - rect.left)/4,
                               rect.y + TILESIZE/2,
                               "Atacar", "withe_button")
    ng_button.draw_button(screen)

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



