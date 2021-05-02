import pygame
import settings
from settings import *
import buttons
import map
import random as rnd
from pygame import mixer
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
                pygame.quit()
                sys.exit()
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
        sound_button = buttons.Button(settings.MARGIN,
                                      settings.MARGIN + settings.BT_HEIGHT,
                                      "Áudio", "blue_button")
        back_button.draw_button(self.scn)
        sound_button.draw_button(self.scn)
        smallfont = pygame.font.Font(f'fonts/{settings.BT_FONT}.ttf', 26)
        text = smallfont.render("Configurações de Jogo:", True, (29, 13, 64))
        self.scn.blit(text, (50, 80))

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        music_setting_button = buttons.Button(settings.MARGIN + 2 * settings.BT_DIST,
                                              settings.MARGIN + settings.BT_HEIGHT,
                                              "Music", "blue_button")
        music_setting_button_on = buttons.Button(settings.MARGIN + settings.BT_DIST,
                                                 settings.MARGIN + settings.BT_HEIGHT,
                                                 "Infantaria", "blue_button")
        music_setting_button_off = buttons.Button(settings.MARGIN + 3 * settings.BT_DIST,
                                                  settings.MARGIN + settings.BT_HEIGHT,
                                                  "Avante", "blue_button")
        music_setting_button_on.draw_button(self.scn)
        music_setting_button.draw_button(self.scn)
        music_setting_button_off.draw_button(self.scn)
        dificuldade_setting_button = buttons.Button(settings.MARGIN + 2 * settings.BT_DIST,
                                                    settings.MARGIN + 2 * settings.BT_HEIGHT,
                                                    "Nível", "blue_button")
        dificuldade_setting_button_on = buttons.Button(settings.MARGIN + settings.BT_DIST,
                                                       settings.MARGIN + 2 * settings.BT_HEIGHT,
                                                       "Facil", "blue_button")
        dificuldade_setting_button_off = buttons.Button(settings.MARGIN + 3 * settings.BT_DIST,
                                                        settings.MARGIN + 2 * settings.BT_HEIGHT,
                                                        "Difícil", "blue_button")
        dificuldade_setting_button_on.draw_button(self.scn)
        dificuldade_setting_button.draw_button(self.scn)
        dificuldade_setting_button_off.draw_button(self.scn)
        if music_setting_button.rectangle.collidepoint((mx, my)):
            if click:
                pass
        if music_setting_button_on.rectangle.collidepoint((mx, my)):
            if click:
                self.clickstate(music_setting_button_on)
                mixer.music.load('../extras/cancao_da_infantaria.WAV')
                mixer.music.play(-1)
        if music_setting_button_off.rectangle.collidepoint((mx, my)):
            if click:
                self.clickstate(music_setting_button_off)
                mixer.music.load('../extras/avante_camaradas.WAV')
                mixer.music.play(-1)
        if dificuldade_setting_button.rectangle.collidepoint((mx, my)):
            if click:
                pass
        if dificuldade_setting_button_on.rectangle.collidepoint((mx, my)):
            if click:
                self.clickstate(dificuldade_setting_button_on)

        if dificuldade_setting_button_off.rectangle.collidepoint((mx, my)):
            if click:
                self.clickstate(dificuldade_setting_button_off)
        # TODO: Antes de dar push, organizar essa implementacao do quit button
        if back_button.rectangle.collidepoint((mx, my)):
            if click:
                back_button.button_img = pygame.transform.scale(
                    pygame.image.load(f'img/buttons/green_button.png'),
                    (settings.BT_WIDTH, settings.BT_HEIGHT))
                back_button.draw_button(self.scn)
                title_screen = TitleScreen()
                running = title_screen.run(running)

        return running, state

    def run(self, running):
        while running:
            self.scn.blit(self.bg, (0, 0))
            if self.state != "":
                running, self.state = self.run_events(running, self.state)
            else:
                running, self.state = self.run_events(running)
            pygame.display.update()

    def clickstate(self,button):
        button.button_img = pygame.transform.scale(
            pygame.image.load(f'img/buttons/green_button.png'),
            (settings.BT_WIDTH, settings.BT_HEIGHT))
        button.draw_button(self.scn)
class ControlsScreen(Screen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Screen.set_bg(self, "bg_control_screen.png")  # mundando a tela para tela de instruções

    def run_events(self, running):
        mx, my = pygame.mouse.get_pos()

        back_button = quit_button = buttons.Button(settings.MARGIN + 3*settings.BT_DIST,
                                   settings.SCREEN_HEIGHT - settings.MARGIN,
                                   "Voltar", "blue_button")

        back_button.draw_button(self.scn)

        #font = pygame.font.Font("fonts/chalkduster.ttf", 60)
        #text = font.render("Desenvolvimento futuro.", True, (29, 13, 64))
        #self.scn.blit(text, (50, 80))

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
        self.key = rnd.randint(30, 200)

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
        linespace = 35
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
                        line += 1
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


def pop_up(player, enemy, screen, qa, itens_icon):
    tempo = pygame.time.Clock();
    ms = 1000
    time_lim = 10*ms
    answered, correct = False, False
    question, ans = qa.get_qa(enemy.level)
    sample = rnd.sample(range(0, 3), 3)
    bg = pygame.transform.scale(pygame.image.load("img/background/battle_alt.png"),
                                (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    while time_lim >= 0:
        screen.blit(bg, (0, 0))
        font = pygame.font.Font(f'fonts/{BT_FONT}.ttf', 30)

        playerSurface = pygame.Surface((SCREEN_WIDTH, 1.2 * TILESIZE))
        playerSurface.set_alpha(0)  # alpha level
        playerSurface.fill(BLACK)  # this fills the entire surface
        rect_player = playerSurface.get_rect(midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT))

        pl_life_text = font.render('Vida:', True, WHITE)
        vida_text = pl_life_text.get_rect(midleft=(TILESIZE / 2, rect_player.center[1]))

        pl_life = font.render(str(player.life), True, RED)
        vida = pl_life.get_rect(midleft=(vida_text.right, rect_player.center[1]))

        bg_itens = pygame.image.load("img/map/inventario.png")

        filter = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        filter.set_alpha(128)  # alpha level
        filter.fill(BLACK)  # this fills the entire surface
        rect_filter = filter.get_rect(midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT))

        screen.blit(filter, rect_filter)
        screen.blit(bg_itens, rect_player)
        screen.blit(pl_life_text, vida_text)
        screen.blit(pl_life, vida)

        # Title
        img = font.render('Combate', True, WHITE)
        rect = img.get_rect(center=(SCREEN_WIDTH / 2, TILESIZE))
        screen.blit(img, rect)

        # Enemy Life
        jogador = font.render("Inimigo", True, WHITE)
        enemy_title = jogador.get_rect(bottomright=(SCREEN_WIDTH - TILESIZE, 3*TILESIZE))

        pl_life = font.render('Vida:', True, WHITE)
        vida = pl_life.get_rect(bottomleft=(enemy_title.left, 3 * TILESIZE))
        #screen.blit(pl_life, vida)

        pl_life = font.render(str(enemy.life), True, RED)
        vida = pl_life.get_rect(bottomleft=(vida.right, 3 * TILESIZE))
        screen.blit(pl_life, vida)

        # Rect for actions
        rect = pygame.Rect(50, 60, SCREEN_WIDTH - 2 * TILESIZE, 0.4 * SCREEN_HEIGHT)
        rect.midbottom = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - TILESIZE / 4)

        # Buttons
        position_x = (SCREEN_WIDTH - BT_WIDTH)/2
        position_y = rect.y + rect.h/2 - TILESIZE/8
       # print(sample, ans)

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

        pos_center = []
        for i in range(0,5):
            position = (700 + 108*i, rect_player.midleft[1])
            pos_center.append(position)

        for i in range(0, 5):
            itens_icon[i].update(player.itens[i], screen)

        # mouse position
        mx, my = pygame.mouse.get_pos()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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
            if itens_icon[0].rectangle.collidepoint((mx, my)) and player.itens[0] > 0:
                time_lim += 10 * ms
                player.itens[0] -= 1
            if itens_icon[1].rectangle.collidepoint((mx, my)) and player.itens[1] > 0:
                time_lim += 2 * ms
                player.itens[1]-= 1
            if itens_icon[2].rectangle.collidepoint((mx, my)) and player.itens[2] > 0:
                time_lim += 2 * ms
                player.itens[2]-= 1
            if itens_icon[3].rectangle.collidepoint((mx, my)) and player.itens[3] > 0:
                time_lim += 2 * ms
                player.itens[3]-= 1
            if itens_icon[4].rectangle.collidepoint((mx, my)) and player.itens[4] > 0:
                time_lim += 2 * ms
                player.itens[4]-= 1

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


def pop_up_final_question(player, enemy, screen, qa):
    bg = pygame.transform.scale(
        pygame.image.load("img/background/battle_alt.png"),
        (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    screen.blit(bg, (0, 0))

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


def gameover(screen):
    screen.fill(BGCOLOR)
    font = pygame.font.Font(f'fonts/{BT_FONT}.ttf', 80)
    # Title
    img = font.render('Game Over', True, WHITE)
    rect = img.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2))
    screen.blit(img, rect)
    pygame.display.flip()


def end_animated_text(scn):
    global text_surface, text_rect

    poema1 = "Se..."
    poema2 = " "
    poema3 = "Se és capaz de manter tua calma, quando,"
    poema4 = "todo mundo ao redor já a perdeu e te culpa."
    poema5 = "De crer em ti quando estão todos duvidando,"
    poema6 = "e para esses no entanto achar uma desculpa."
    poema7 = "és um Homem, meu filho!"

    full_end_list = [poema1, poema2, poema3, poema4, poema5, poema6, poema7]

    smallfont = pygame.font.Font(f'fonts/{settings.BT_FONT}.ttf', 22)
    text = ''
    surfaces_list = []
    linespace = 35
    line = 0
    skip = False

    for intro in full_end_list:
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
                for intro_line in full_end_list:
                    text_surface = smallfont.render(intro_line, True, WHITE)
                    text_rect = text_surface.get_rect()
                    text_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + (line - 3) * linespace)
                    line += 1
                    s = (text_surface, text_rect)
                    surfaces_list.append(s)
                continue

            scn.fill(BLACK)
            for s in surfaces_list:
                scn.blit(*s)
            text += intro[i]
            text_surface = smallfont.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 3 * linespace + line * linespace)
            scn.blit(text_surface, text_rect)
            pygame.display.update()
            pygame.time.wait(40)

        if skip:
            break
        else:
            s = (text_surface, text_rect)
            line += 1
            surfaces_list.append(s)
            text = ''

    scn.fill(BLACK)
    for s in surfaces_list:
        scn.blit(*s)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return

def end_participantes(scn):
    global text_surface, text_rect

    poema1 = "Participantes:"
    poema2 = "Arthur José - Pagodinho"
    poema3 = "Fernando Zanchitta - Zank"
    poema4 = "Gabriel Gobi - Gobi"
    poema5 = "Guilherme Kowalczuk - Kowa"
    poema6 = "Thiago Lopes - TH"
    poema7 = "Yuri Gama - Índio"

    full_end_list = [poema1, poema2, poema3, poema4, poema5, poema6, poema7]

    smallfont = pygame.font.Font(f'fonts/{settings.BT_FONT}.ttf', 22)
    text = ''
    surfaces_list = []
    linespace = 50
    line = 0
    skip = False

    for intro in full_end_list:
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
                for intro_line in full_end_list:
                    text_surface = smallfont.render(intro_line, True, WHITE)
                    text_rect = text_surface.get_rect()
                    text_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + (line - 3) * linespace)
                    line += 1
                    s = (text_surface, text_rect)
                    surfaces_list.append(s)
                continue

            scn.fill(BLACK)
            for s in surfaces_list:
                scn.blit(*s)
            text += intro[i]
            text_surface = smallfont.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 3 * linespace + line * linespace)
            scn.blit(text_surface, text_rect)
            pygame.display.update()
            pygame.time.wait(40)

        if skip:
            break
        else:
            s = (text_surface, text_rect)
            line += 1
            surfaces_list.append(s)
            text = ''

    scn.fill(BLACK)
    for s in surfaces_list:
        scn.blit(*s)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return