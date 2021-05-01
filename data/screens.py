import pygame
import settings
from settings import *
import buttons
import map
import random as rnd

class Screen():
    """ Class of a generic screen in the game """
    def __init__(self, caption = "My game name", *args, **kwargs):
        # Initialize screen
        self.scn = pygame.display.set_mode((settings.SCREEN_WIDTH,
                                               settings.SCREEN_HEIGHT))
        # Load default background
        self.bg = pygame.transform.scale( # TODO: remove this when all bg defined
            pygame.image.load("img/background/capa.png"),
            (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

        # Load caption of the screen (game name by default)
        pygame.display.set_caption(caption)
        
    def set_bg(self, bg_str):
        self.bg = pygame.transform.scale(
            pygame.image.load(f'img/background/{bg_str}'),
            (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        )

    def run(self, running):
        """ Load and update a specified screen """
        while running:
            self.scn.blit(self.bg, (0, 0))
            running = self.run_events(running)
            pygame.display.update()

    def run_events(self, running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            return running

class TitleScreen(Screen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run_events(self, running):

        mx, my = pygame.mouse.get_pos()

        ng_button = buttons.Button(settings.MARGIN,
                                   settings.SCREEN_HEIGHT-settings.MARGIN,
                                   "Novo jogo", "blue_button")
        controls_button = buttons.Button(settings.MARGIN + settings.BT_DIST,
                                   settings.SCREEN_HEIGHT - settings.MARGIN,
                                   "Controles", "blue_button")
        settings_button = buttons.Button(settings.MARGIN + 2*settings.BT_DIST,
                                   settings.SCREEN_HEIGHT - settings.MARGIN,
                                   "Opções", "blue_button")
        quit_button = buttons.Button(settings.MARGIN + 3*settings.BT_DIST,
                                   settings.SCREEN_HEIGHT - settings.MARGIN,
                                   "Sair", "blue_button")

        ng_button.draw_button(self.scn)
        controls_button.draw_button(self.scn)
        settings_button.draw_button(self.scn)
        quit_button.draw_button(self.scn)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # TODO: create click function in the Button class
        if ng_button.rectangle.collidepoint((mx, my)):
            if click:
                game_screen = GameScreen()
                game_screen.intro_animated_text()
                game_screen.password_text()
                running = game_screen.run(running)
        if controls_button.rectangle.collidepoint((mx, my)):
            if click:
                controls_screen = ControlsScreen()
                running = controls_screen.run(running)
        if settings_button.rectangle.collidepoint((mx, my)):
            if click:
                setting_screen = SettingsScreen()
                running, state = setting_screen.run(running)
        if quit_button.rectangle.collidepoint((mx, my)):
            if click:
                running = False
                pygame.quit()
                sys.exit()

        return running

class SettingsScreen(Screen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = ""

    def run_events(self, running, state = "Default"):
        mx, my = pygame.mouse.get_pos()
        back_button = buttons.Button(settings.MARGIN + 3 * settings.BT_DIST,
                                     settings.SCREEN_HEIGHT - settings.MARGIN,
                                     "Voltar", "blue_button")
        video_button = buttons.Button(settings.MARGIN,
                                      settings.MARGIN,
                                      "Vídeo", "blue_button")
        sound_button = buttons.Button(settings.MARGIN,
                                      settings.MARGIN + settings.BT_HEIGHT,
                                      "Áudio", "blue_button")
        video_button.draw_button(self.scn)
        back_button.draw_button(self.scn)
        sound_button.draw_button(self.scn)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if state == "Vídeo":
            video_setting_button_type1 = buttons.Button(settings.MARGIN + 2 * settings.BT_DIST,
                                                        settings.SCREEN_HEIGHT - settings.MARGIN,
                                                        "Default", "blue_button")
            video_setting_button_type2 = buttons.Button(settings.MARGIN+ 2 * settings.BT_DIST,
                                                        settings.MARGIN,
                                                        "2560x1600", "blue_button")
            video_setting_button_type3 = buttons.Button(settings.MARGIN + 2 * settings.BT_DIST,
                                                        settings.MARGIN + settings.BT_HEIGHT+1,
                                                        "800x600", "blue_button")
            video_setting_button_type1.draw_button(self.scn)
            video_setting_button_type2.draw_button(self.scn)
            video_setting_button_type3.draw_button(self.scn)
            if video_setting_button_type1.rectangle.collidepoint((mx, my)):
                if click:
                    video_setting_button_type1.button_img = pygame.transform.scale(
                        pygame.image.load(f'img/buttons/green_button.png'),
                        (settings.BT_WIDTH, settings.BT_HEIGHT))
                    video_setting_button_type1.draw_button(self.scn)
            if video_setting_button_type2.rectangle.collidepoint((mx, my)):
                if click:
                    video_setting_button_type2.button_img = pygame.transform.scale(
                        pygame.image.load(f'img/buttons/green_button.png'),
                        (settings.BT_WIDTH, settings.BT_HEIGHT))
                    video_setting_button_type2.draw_button(self.scn)
            if video_setting_button_type3.rectangle.collidepoint((mx, my)):
                if click:
                    video_setting_button_type3.button_img = pygame.transform.scale(
                        pygame.image.load(f'img/buttons/green_button.png'),
                        (settings.BT_WIDTH, settings.BT_HEIGHT))
                    video_setting_button_type3.draw_button(self.scn)
        if state == "Áudio":
            music_setting_button = buttons.Button(settings.MARGIN + 2*settings.BT_DIST,
                                                  settings.MARGIN + settings.BT_HEIGHT,
                                                  "Music", "blue_button")
            music_setting_button_on = buttons.Button(settings.MARGIN + settings.BT_DIST,
                                                     settings.MARGIN + settings.BT_HEIGHT,
                                                     "ON", "blue_button")
            music_setting_button_off = buttons.Button(settings.MARGIN+ 3* settings.BT_DIST,
                                                      settings.MARGIN + settings.BT_HEIGHT,
                                                      "OFF", "blue_button")
            sound_setting_button = buttons.Button(settings.MARGIN + 2 * settings.BT_DIST,
                                                  settings.MARGIN + 2*settings.BT_HEIGHT+10,
                                                  "Music", "blue_button")
            sound_setting_button_on = buttons.Button(settings.MARGIN + settings.BT_DIST,
                                                     settings.MARGIN + 2*settings.BT_HEIGHT+10,
                                                     "ON", "blue_button")
            sound_setting_button_off = buttons.Button(settings.MARGIN + 3 * settings.BT_DIST,
                                                      settings.MARGIN + 2*settings.BT_HEIGHT+10,
                                                      "OFF", "blue_button")
            music_setting_button_on.draw_button(self.scn)
            music_setting_button.draw_button(self.scn)
            music_setting_button_off.draw_button(self.scn)
            sound_setting_button_on.draw_button(self.scn)
            sound_setting_button.draw_button(self.scn)
            sound_setting_button_off.draw_button(self.scn)
            if music_setting_button.rectangle.collidepoint((mx, my)):
                if click:
                    pass
            if music_setting_button_on.rectangle.collidepoint((mx, my)):
                if click:
                    music_setting_button_on.button_img = pygame.transform.scale(
                        pygame.image.load(f'img/buttons/green_button.png'),
                        (settings.BT_WIDTH, settings.BT_HEIGHT))
                    music_setting_button_on.draw_button(self.scn)
            if music_setting_button_off.rectangle.collidepoint((mx, my)):
                if click:
                    music_setting_button_off.button_img = pygame.transform.scale(
                        pygame.image.load(f'img/buttons/green_button.png'),
                        (settings.BT_WIDTH, settings.BT_HEIGHT))
                    music_setting_button_off.draw_button(self.scn)
            if sound_setting_button.rectangle.collidepoint((mx, my)):
                if click:
                    pass
            if sound_setting_button_on.rectangle.collidepoint((mx, my)):
                if click:
                    sound_setting_button_on.button_img = pygame.transform.scale(
                        pygame.image.load(f'img/buttons/green_button.png'),
                        (settings.BT_WIDTH, settings.BT_HEIGHT))
                    sound_setting_button_on.draw_button(self.scn)
            if sound_setting_button_off.rectangle.collidepoint((mx, my)):
                if click:
                    sound_setting_button_off.button_img = pygame.transform.scale(
                        pygame.image.load(f'img/buttons/green_button.png'),
                        (settings.BT_WIDTH, settings.BT_HEIGHT))
                    sound_setting_button_off.draw_button(self.scn)
        # TODO: Antes de dar push, organizar essa implementacao do quit button
        if back_button.rectangle.collidepoint((mx, my)):
            if click:
                title_screen = TitleScreen()
                running = title_screen.run(running)
        if video_button.rectangle.collidepoint((mx, my)):
            if click:
                state = "Vídeo"
        if sound_button.rectangle.collidepoint((mx, my)):
            if click:
                state = "Áudio"

        return running, state

    def run(self, running):
        while running:
            self.scn.blit(self.bg, (0, 0))
            if self.state != "":
                running, self.state = self.run_events(running, self.state)
            else:
                running, self.state = self.run_events(running)
            pygame.display.update()

class ControlsScreen(Screen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run_events(self, running):

        mx, my = pygame.mouse.get_pos()

        back_button = quit_button = buttons.Button(settings.MARGIN + 3*settings.BT_DIST,
                                   settings.SCREEN_HEIGHT - settings.MARGIN,
                                   "Voltar", "blue_button")

        back_button.draw_button(self.scn)
        font = pygame.font.Font("fonts/chalkduster.ttf", 60)
        text = font.render("Desenvolvimento futuro.", True, (29, 13, 64))
        self.scn.blit(text, (50, 80))

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if back_button.rectangle.collidepoint((mx, my)):
            if click:
                title_screen = TitleScreen()
                running = title_screen.run(running)

        return running

class GameScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.key = rnd.randint(0, 200)

    def run_events(self, running):
        game_map = map.Map(self.scn, self.key)
        running = game_map.run(self.scn, True)
        return running

    def intro_animated_text(self):
        global text_surface, text_rect

        intro1 = "Em mais um dia de campanha, o militar mais padrão de todos é posto a prova."
        intro2 = "Fuja da área de acampamento sem ser pego pelos sargentos."
        intro3 = "Para ser considerado padrão, o Zero-zero-um deve responder a senha correta."
        full_intro_list = [intro1, intro2, intro3]

        smallfont = pygame.font.Font(f'fonts/{settings.BT_FONT}.ttf', 22)
        text = ''
        surfaces_list = []
        linespace = 30
        line = 0
        skip = False

        for intro in full_intro_list :
            for i in range(len(intro)):

                # verificando se nao ha skip
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        skip = True
                    continue

                if skip:
                    surfaces_list = []
                    linespace = 30
                    line = 0
                    for intro_line in full_intro_list:
                        text_surface = smallfont.render(intro_line, True, WHITE)
                        text_rect = text_surface.get_rect()
                        text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + (line-1) * linespace)
                        line+=1
                        s = (text_surface, text_rect)
                        surfaces_list.append(s)
                    continue

                self.scn.fill(BLACK)
                for s in surfaces_list:
                    self.scn.blit(*s)
                text += intro[i]
                text_surface = smallfont.render(text, True, WHITE)
                text_rect = text_surface.get_rect()
                text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 -linespace + line*linespace)
                self.scn.blit(text_surface, text_rect)
                pygame.display.update()
                pygame.time.wait(60)

            if skip:
                continue
            else:
                s = (text_surface, text_rect)
                line+=1
                surfaces_list.append(s)
                text = ''

        self.scn.fill(BLACK)
        for s in surfaces_list:
            self.scn.blit(*s)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return

    def password_text(self):
        global text_surface, text_rect

        password_text = f"A senha e a contrasenha somam {self.key}."

        smallfont = pygame.font.Font(f'fonts/{settings.BT_FONT}.ttf', 22)
        text = ''
        skip = False

        for i in range(len(password_text)):

            # verificando se nao ha skip
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    skip = True
                continue

            if skip:
                text_surface = smallfont.render(password_text, True, WHITE)
                text_rect = text_surface.get_rect()
                text_rect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
                continue

            self.scn.fill(BLACK)
            text += password_text[i]
            text_surface = smallfont.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
            self.scn.blit(text_surface, text_rect)
            pygame.display.update()
            pygame.time.wait(60)

        self.scn.fill(BLACK)
        self.scn.blit(text_surface, text_rect)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return


def pop_up(player, enemy, screen, qa):
    tempo = pygame.time.Clock();
    ms = 1000
    time_lim = 10*ms
    answered, correct = False, False
    question, ans = qa.get_qa()
    sample = rnd.sample(range(0, 3), 3)
    bg = pygame.transform.scale(pygame.image.load("img/background/battle_alt.png"),
                                (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    while time_lim >= 0:
        screen.blit(bg, (0, 0))
        font = pygame.font.Font(f'fonts/{BT_FONT}.ttf', 30)
        # Title
        img = font.render('Combate', True, WHITE)
        rect = img.get_rect(center=(SCREEN_WIDTH / 2, TILESIZE))
        screen.blit(img, rect)

        # Players Life
        pl_life = font.render('Vida:', True, WHITE)
        vida = pl_life.get_rect(bottomleft=(TILESIZE, 3 * TILESIZE))
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
        vida = pl_life.get_rect(bottomleft=(enemy_title.left, 3 * TILESIZE))
        screen.blit(pl_life, vida)

        pl_life = font.render(str(enemy.life), True, RED)
        vida = pl_life.get_rect(bottomleft=(vida.right, 3 * TILESIZE))
        screen.blit(pl_life, vida)

        BACK = (70, 70, 70)
        # Rect for actions
        rect = pygame.Rect(50, 60, SCREEN_WIDTH - 2 * TILESIZE, 0.4 * SCREEN_HEIGHT)
        rect.midbottom = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - TILESIZE / 4)
        pygame.draw.rect(screen, BACK, rect, border_radius=10)

        # Buttons
        position_x = rect.x + (rect.right - rect.left) / 4
        position_y = rect.y + rect.h/2 - TILESIZE + TILESIZE/4
        print(sample, ans)
        atck2 = buttons.ButtonFight(position_x,position_y
                                    ,
                                    ans[sample[0]], "withe_button", sample[0])

        space = TILESIZE
        atck1 = buttons.ButtonFight(position_x - atck2.rectangle.w - space,
                                   position_y,
                                   ans[sample[1]], "withe_button", sample[1])

        atck3 = buttons.ButtonFight(position_x + atck2.rectangle.w + space,
                                   position_y,
                                   ans[sample[2]], "withe_button", sample[2])

        atck1.draw_button(screen)
        atck2.draw_button(screen)
        atck3.draw_button(screen)

        itens = font.render("Itens", True, WHITE)
        itenspos = itens.get_rect(midtop=(rect.center[0] + (rect.right - rect.left) / 4, rect.y + TILESIZE / 4))
        screen.blit(itens, itenspos)

        # ITENS
        nTILESIZE = 1.2 * TILESIZE
        rect_itens = pygame.Rect(0, 0, nTILESIZE, nTILESIZE)

        pos_center = []
        for y_off in range(0, 3, 1):
            for x_off in range(0, 3, 1):
                rect_itens.topleft = (
                itenspos.bottomleft[0] + x_off * nTILESIZE, itenspos.bottomleft[1] + y_off * nTILESIZE)
                pos_center.append(rect_itens.center)
                pygame.draw.rect(screen, (50, 50, 50), rect_itens)
                pygame.draw.rect(screen, WHITE, rect_itens, width=1)

        #print(pos_center)
        item1 = buttons.ButtonItens(0, 0, nTILESIZE, pos_center[0], "hp_potion", player.itens[0])
        item2 = buttons.ButtonItens(0, 0, nTILESIZE, pos_center[1], "hp_potion", player.itens[1])
        item3 = buttons.ButtonItens(0, 0, nTILESIZE, pos_center[2], "hp_potion", player.itens[2])
        item4 = buttons.ButtonItens(0, 0, nTILESIZE, pos_center[3], "hp_potion", player.itens[3])
        item5 = buttons.ButtonItens(0, 0, nTILESIZE, pos_center[4], "hp_potion", player.itens[4])
        item6 = buttons.ButtonItens(0, 0, nTILESIZE, pos_center[5], "hp_potion", player.itens[5])
        item7 = buttons.ButtonItens(0, 0, nTILESIZE, pos_center[6], "hp_potion", player.itens[6])
        item8 = buttons.ButtonItens(0, 0, nTILESIZE, pos_center[7], "hp_potion", player.itens[7])
        item9 = buttons.ButtonItens(0, 0, nTILESIZE, pos_center[8], "timer", player.itens[8])

        item1.draw_button(screen)
        item2.draw_button(screen)
        item3.draw_button(screen)
        item4.draw_button(screen)
        item5.draw_button(screen)
        item6.draw_button(screen)
        item7.draw_button(screen)
        item8.draw_button(screen)
        item9.draw_button(screen)

        # mouse position
        mx, my = pygame.mouse.get_pos()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if click:
            if atck1.rectangle.collidepoint((mx, my)):
                answered, correct = True, qa.is_correct(atck1.index)
                break
            if atck2.rectangle.collidepoint((mx, my)):
                answered, correct = True, qa.is_correct(atck2.index)
                break
            if atck3.rectangle.collidepoint((mx, my)):
                answered, correct = True, qa.is_correct(atck3.index)
                break
            if item1.rectangle.collidepoint((mx, my)) and player.itens[0] > 0:
                time_lim += 10 * ms
                player.itens[0] -= 1
            if item2.rectangle.collidepoint((mx, my)) and player.itens[1] > 0:
                time_lim += 2 * ms
                player.itens[1]-= 1
            if item3.rectangle.collidepoint((mx, my)) and player.itens[2] > 0:
                time_lim += 2 * ms
                player.itens[2]-= 1
            if item4.rectangle.collidepoint((mx, my)) and player.itens[3] > 0:
                time_lim += 2 * ms
                player.itens[3]-= 1
            if item5.rectangle.collidepoint((mx, my)) and player.itens[4] > 0:
                time_lim += 2 * ms
                player.itens[4]-= 1
            if item6.rectangle.collidepoint((mx, my)) and player.itens[5] > 0:
                time_lim += 2 * ms
                player.itens[5]-= 1
            if item7.rectangle.collidepoint((mx, my)) and player.itens[6] > 0:
                time_lim += 2 * ms
                player.itens[6]-= 1
            if item8.rectangle.collidepoint((mx, my)) and player.itens[7] > 0:
                time_lim += 2 * ms
                player.itens[7]-= 1
            if item9.rectangle.collidepoint((mx, my)) and player.itens[8] > 0:
                player.itens[8]-= 1
                time_lim += 2 * ms

        text_time = round(time_lim/1000)
        tempo_text = font.render(str(text_time), True, WHITE)
        tempo_title= tempo_text.get_rect(center=(SCREEN_WIDTH / 2, TILESIZE*1.5 + TILESIZE/4))
        screen.blit(tempo_text, tempo_title)
        time_lim -= tempo.tick()

        font_text = pygame.font.Font(f'fonts/{BT_FONT}.ttf', 30)

        # Question Text

        qSurface = pygame.Surface((TILESIZE*10, TILESIZE*4))  # the size of your rect
        qSurface.set_alpha(128)  # alpha level
        qSurface.fill(WHITE)  # this fills the entire surface
        rect = qSurface.get_rect(midtop = (tempo_title.midbottom[0],tempo_title.midbottom[1] + TILESIZE/4))

        question_text = font_text.render(question, True, WHITE)
        question_rect = question_text.get_rect(center= rect.center)

        screen.blit(qSurface, rect)
        screen.blit(question_text, question_rect)

        pygame.display.flip()

        if player.life <=0 or enemy.life <=0:
            break

    if not answered or not correct:
        player.life -= 10
    if answered and correct:
        enemy.life -= 10

def gameover(screen):
    screen.fill(BGCOLOR)
    font = pygame.font.Font(f'fonts/{BT_FONT}.ttf', 80)
    # Title
    img = font.render('Game Over', True, WHITE)
    rect = img.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2))
    screen.blit(img, rect)
    pygame.display.flip()
