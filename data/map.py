import pygame
from player import *
from wall import *
from room import *
import buttons
import screens as scn
import itens
from qa import *
from password import *

class Map:
    def __init__(self, screen, key):
        self.key = key
        self.password = Password()
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500,50)
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.my_player = Player(5, 5, self.walls)
        self.all_sprites.add(self.my_player)
        self.map_image, self.room_tmx = self.set_rooms()
        self.map_image = pygame.transform.scale(self.map_image, (MAPSIZE*ROOMSIZE*TILESIZE,MAPSIZE*ROOMSIZE*TILESIZE))
        self.map_rect = self.map_image.get_rect()
        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.key_sprites = pygame.sprite.Group()
        self.my_key = itens.KeyItem(self.all_sprites, self.key_sprites, self.my_player, 25 , 8)

        # self.clock_sprites = pygame.sprite.Group() # aumenta o tempo de limite de resposta para todas perguntas (ponteiro)
        # self.my_clock = itens.ClockItem(self.all_sprites, self.clock_sprites, self.my_player, 1, 2)
        #
        # self.heal_low_sprites = pygame.sprite.Group() # aumenta um pouco a vida (cantil semicheio)
        # self.my_heal_low = itens.HealItem(self.all_sprites, self.heal_low_sprites, self.my_player, 1, 3)
        #
        # self.heal_medium_sprites = pygame.sprite.Group() # aumenta um pouco mais a vida (cantil pleno)
        # self.my_heal_medium = itens.AdvancedHealItem(self.all_sprites, self.heal_medium_sprites, self.my_player, 1, 4)
        #
        # self.life_improve_sprites = pygame.sprite.Group() # congela o tempo para uma pergunta (relogio com neve)
        # self.my_life_improve = itens.ImproveLifeItem(self.all_sprites, self.life_improve_sprites, self.my_player, 1, 5)
        #
        # self.attack_low_sprites = pygame.sprite.Group() # dá um dano pequeno no inimigo (ripa de madeira)
        # self.my_attack_low = itens.AttackItem(self.all_sprites, self.attack_low_sprites, self.my_player, 2, 1)
        #
        # self.attack_medium_sprites = pygame.sprite.Group() # dá um dano medio no inimigo (boot)
        # self.my_attack_medium = itens.AdvancedAttackItem(self.all_sprites, self.attack_medium_sprites, self.my_player, 2, 2)
        #
        # self.supreme_sprites = pygame.sprite.Group() # derrota o inimigo instantaneamente (em off)
        # self.my_supreme = itens.SupremeItem(self.all_sprites, self.supreme_sprites, self.my_player, 2, 3)
        #
        # self.attack_improve_sprites = pygame.sprite.Group() # aumenta o dano dado por resposta correta (livro)
        # self.my_attack_improve = itens.ImproveAttackItem(self.all_sprites, self.attack_improve_sprites, self.my_player, 2, 4)
        #
        # self.defence_sprites = pygame.sprite.Group() # dá uma chance de errar/passar tempo sem perder vida (colete)
        # self.my_defence = itens.DefenceItem(self.all_sprites, self.defence_sprites, self.my_player, 2, 5)

        self.enemies = pygame.sprite.Group()
        self.spawn_enemies()

        self.my_itens = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.dt = 0
        self.qa = QA(self.key)

    def set_rooms(self):
        all_room_img = pygame.Surface((MAPSIZE*ROOMSIZE*ROOMSIZE, MAPSIZE*ROOMSIZE*ROOMSIZE))
        room_list = [[TiledRoom("Spawnpoint"), TiledRoom("map_template_up_middle"), TiledRoom("before_end"), TiledRoom("End_room")],
                     [TiledRoom("passagem_up_left"),TiledRoom("map_template_bottom_middle"), TiledRoom("only_right"), TiledRoom("key_room")],
                     [TiledRoom("map_template_bottom_left"), TiledRoom("map_template_up_right"), TiledRoom("map_template_up_left"), TiledRoom("map_template_bottom_right")],
                     [TiledRoom("only_left"), TiledRoom("map_template_bottom_middle"), TiledRoom("map_template_bottom_middle"), TiledRoom("only_right")]]
        for row in range(MAPSIZE):
            for col in range(MAPSIZE):
                all_room_img = room_list[row][col].make_room(all_room_img, col, row)
                for tile_object in room_list[row][col].tmxdata.objects:
                    if tile_object.name == 'Wall':
                        # print(tile_object.x,tile_object.y,tile_object.width,tile_object.height)
                        Obstacle(self.walls, tile_object.x*4 + col * ROOMSIZE*TILESIZE,tile_object.y*4 + row * ROOMSIZE * TILESIZE, tile_object.width*4, tile_object.height*4)
        return all_room_img, room_list

    def run(self, screen, running):
        while running:
            self.dt = self.clock.tick(FPS)/1000
            running = self.event(running)
            self.draw(screen)
            if self.my_player.life <= 0:
                pygame.time.wait(2000)
                break

    def draw(self, screen):
        screen.fill(BLACK)

        screen.blit(self.map_image, self.camera.apply_rect(self.map_rect))

        for sprite in self.all_sprites:
            screen.blit(sprite.image, self.camera.apply(sprite))

        self.draw_info(screen)
        self.check_collision(screen)

        pygame.display.flip()

    # def draw_grid(self, screen):
    #     for y_offset in range(0, SCREEN_HEIGHT, TILESIZE):
    #         pygame.draw.line(screen, LIGHTGREY, (0,y_offset), (SCREEN_WIDTH, y_offset))
    #     for x_offset in range(0, SCREEN_WIDTH, TILESIZE):
    #         pygame.draw.line(screen, LIGHTGREY, (x_offset, 0), (x_offset, SCREEN_WIDTH))

    def event(self, running):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.my_player.move(1, 0)
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.my_player.move(-1, 0)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.my_player.move(0, -1)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.my_player.move(0, 1)
        elif keys[pygame.QUIT]:
            running = False
        else:
            self.my_player.stop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        self.all_sprites.update()
        self.camera.update(self.my_player)
        # pygame.sprite.spritecollide(self.my_player, self.enemies, 1)
        return running

    def check_collision(self, screen):
        for enemy in self.enemies:
            if abs(self.my_player.rect.x - enemy.rect.x) < TILESIZE and \
                    abs(self.my_player.rect.y - enemy.rect.y) < TILESIZE:
                while enemy.life > 0 and self.my_player.life > 0:
                    scn.pop_up(self.my_player, enemy, screen, self.qa)
                if enemy.life <= 0:
                    enemy.kill()
                break

        if self.my_player.life <= 0:
            scn.gameover(screen)

        for key in self.key_sprites:
            if abs(self.my_player.rect.x - key.rect.x) < TILESIZE and \
                    abs(self.my_player.rect.y - key.rect.y) < TILESIZE:
                self.my_key.show_key_password(screen, self.password)


        # for clock in self.clock_sprites:
        #     if abs(self.my_player.rect.x - clock.rect.x) < TILESIZE and \
        #             abs(self.my_player.rect.y - clock.rect.y) < TILESIZE:
        #         self.my_player.itens[3]+= 1
        #         print(self.my_player.itens)
        #         clock.kill()
        #
        # for heal_low in self.heal_low_sprites:
        #     if abs(self.my_player.rect.x - heal_low.rect.x) < TILESIZE and \
        #             abs(self.my_player.rect.y - heal_low.rect.y) < TILESIZE:
        #         self.my_player.itens[0]+= 1
        #         print(self.my_player.itens)
        #         heal_low.kill()
        #
        # for heal_medium in self.heal_medium_sprites:
        #     if abs(self.my_player.rect.x - heal_medium.rect.x) < TILESIZE and \
        #             abs(self.my_player.rect.y - heal_medium.rect.y) < TILESIZE:
        #         self.my_player.itens[1]+= 1
        #         print(self.my_player.itens)
        #         heal_medium.kill()
        #
        # for life_improve in self.life_improve_sprites:
        #     if abs(self.my_player.rect.x - life_improve.rect.x) < TILESIZE and \
        #             abs(self.my_player.rect.y - life_improve.rect.y) < TILESIZE:
        #         self.my_player.itens[2]+= 1
        #         print(self.my_player.itens)
        #         life_improve.kill()
        #
        # for defence in self.defence_sprites:
        #     if abs(self.my_player.rect.x - defence.rect.x) < TILESIZE and \
        #             abs(self.my_player.rect.y - defence.rect.y) < TILESIZE:
        #         self.my_player.itens[4]+= 1
        #         print(self.my_player.itens)
        #         defence.kill()
        #
        # for attack_low in self.attack_low_sprites:
        #     if abs(self.my_player.rect.x - attack_low.rect.x) < TILESIZE and \
        #             abs(self.my_player.rect.y - attack_low.rect.y) < TILESIZE:
        #         self.my_player.itens[6]+= 1
        #         print(self.my_player.itens)
        #         attack_low.kill()
        #
        # for attack_medium in self.attack_medium_sprites:
        #     if abs(self.my_player.rect.x - attack_medium.rect.x) < TILESIZE and \
        #             abs(self.my_player.rect.y - attack_medium.rect.y) < TILESIZE:
        #         self.my_player.itens[7]+= 1
        #         print(self.my_player.itens)
        #         attack_medium.kill()
        #
        # for attack_improve in self.attack_improve_sprites:
        #     if abs(self.my_player.rect.x - attack_improve.rect.x) < TILESIZE and \
        #             abs(self.my_player.rect.y - attack_improve.rect.y) < TILESIZE:
        #         self.my_player.itens[8]+= 1
        #         print(self.my_player.itens)
        #         attack_improve.kill()
        #
        # for supreme in self.supreme_sprites:
        #     if abs(self.my_player.rect.x - supreme.rect.x) < TILESIZE and \
        #             abs(self.my_player.rect.y - supreme.rect.y) < TILESIZE:
        #         self.my_player.itens[5] = 1
        #         print(self.my_player.itens)
        #         supreme.kill()

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

    # TODO: read spawn locations for data
    def spawn_enemies(self):
        self.my_enemy = Enemy(self.walls, self.all_sprites, self.enemies,
                              self.my_player, 7, 7, 41)
        self.my_enemy = Enemy(self.walls, self.all_sprites, self.enemies,
                              self.my_player, 5, 6, 54)
        self.my_enemy = Enemy(self.walls, self.all_sprites, self.enemies,
                              self.my_player, 7, 7, 545)
        self.my_enemy = Enemy(self.walls, self.all_sprites, self.enemies,
                              self.my_player, 7, 8, 13)
        self.my_enemy = Enemy(self.walls, self.all_sprites, self.enemies,
                              self.my_player, 10, 7, 80)
        self.my_enemy = Enemy(self.walls, self.all_sprites, self.enemies,
                              self.my_player, 7, 11, 899)

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
