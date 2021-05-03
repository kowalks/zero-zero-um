import random as rnd
import pygame
import textinput
import buttons
from settings import *

class Password:
    def __init__(self, *args, **kwargs):
        self.airplane_n = rnd.randint(21, 29)
        self.departure_time = rnd.randint(6, 9)
        self.sigsauer_rifles = rnd.randint(10, 99)
        self.atomic_bombs = rnd.randint(20, 45)
        self.lmg_rifles = rnd.randint(2, 5)
        self.lmg_caliber = rnd.choice([22, 30, 40, 45, 50])
        self.arrival_time = rnd.randint(13, 21)

    def show_key_password(self, screen):
        keySurface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        keySurface.set_alpha(128)  # alpha level
        keySurface.fill(BLACK)  # this fills the entire surface
        keyRect = keySurface.get_rect()
        screen.blit(keySurface, keyRect)
        smallfont = pygame.font.Font(f'fonts/{BT_FONT}.ttf', 22)

        message_l1 = f"Uma aeronave AT-{self.airplane_n}, saindo da base aérea de UET, às {self.departure_time}h"
        message_l2 = f"de Zulu carregando {self.sigsauer_rifles} fuzis SigSauer e {self.atomic_bombs} bombas atômicas"
        message_l3 = f"e {self.lmg_rifles} metralhadoras .{self.lmg_caliber} devendo chegar às {self.arrival_time}h em Zulu"

        full_message = [message_l1, message_l2, message_l3]

        surfaces_list = []
        linespace = 30
        line_number = 0
        for line in full_message:
            text_surface = smallfont.render(line, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.center = (
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + (line_number - 1) * linespace)
            line_number += 1
            s = (text_surface, text_rect)
            surfaces_list.append(s)
        for s in surfaces_list:
            screen.blit(*s)


    def enter_password_screen(self, screen, player):
        times_pressed = 0
        answered, correct = False, False
        answers = []

        click = False

        bg = pygame.transform.scale(
            pygame.image.load("img/background/battle_alt.png"),
            (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(bg, (0, 0))
        font = pygame.font.Font(f'fonts/{BT_FONT}.ttf', 30)

        playerSurface = pygame.Surface((SCREEN_WIDTH, 1.2 * TILESIZE))
        playerSurface.set_alpha(0)  # alpha level
        playerSurface.fill(BLACK)  # this fills the entire surface
        rect_player = playerSurface.get_rect(
            midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT))

        pl_life_text = font.render('Vida:', True, WHITE)
        vida_text = pl_life_text.get_rect(
            midleft=(TILESIZE / 2, rect_player.center[1]))

        pl_life = font.render(str(player.life), True, RED)
        vida = pl_life.get_rect(
            midleft=(vida_text.right, rect_player.center[1]))

        filter = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        filter.set_alpha(128)  # alpha level
        filter.fill(BLACK)  # this fills the entire surface
        rect_filter = filter.get_rect(
            midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT))

        screen.blit(filter, rect_filter)
        screen.blit(pl_life_text, vida_text)
        screen.blit(pl_life, vida)

        # Title
        title_img = font.render('Qual a mensagem?', True, WHITE)
        title_rect = title_img.get_rect(center=(SCREEN_WIDTH / 2, TILESIZE))
        screen.blit(title_img, title_rect)


        # Question Text
        qSurface = pygame.Surface((TILESIZE * 15, TILESIZE * 4))  # the size of your rect
        qSurface.set_alpha(128)  # alpha level
        qSurface.fill(WHITE)  # this fills the entire surface
        qRect = qSurface.get_rect(midtop=(640, 143))
        screen.blit(qSurface, qRect)

        # Back Button
        back_button = buttons.ButtonFight(1000,600 , "Voltar", "withe_button")
        back_button.draw_button(screen)

        smallfont = pygame.font.Font(f'fonts/{BT_FONT}.ttf', 22)

        message_l1 = f"Uma aeronave AT-     , saindo da base aérea de UET, às    h"
        message_l2 = f"de Zulu carregando      fuzis SigSauer e      bombas atômicas"
        message_l3 = f"e      metralhadoras .      devendo chegar às      h em Zulu"

        full_message = [message_l1, message_l2, message_l3]

        surfaces_list = []
        linespace = 30
        line_number = 0
        for line in full_message:
            text_surface = smallfont.render(line, True, WHITE)
            text_rect = text_surface.get_rect(center= (640, 271 + (line_number - 1) * linespace))
            line_number += 1
            s = (text_surface, text_rect)
            surfaces_list.append(s)
        for s in surfaces_list:
            screen.blit(*s)

        # Password inputs
        text_input = textinput.TextInput(
            font_family=f'fonts/{BT_FONT}.ttf',
            font_size=22,
            text_color=ARMY_GREEN)

        answers_surfaces_list = []
        answer_rect = (480, 230)
        while not answered:
            events = pygame.event.get()

            # mouse position
            mx, my = pygame.mouse.get_pos()

            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
                    times_pressed += 1
                    answers.append(int(text_input.get_text()))
                    s = (text_input.get_surface(), answer_rect)
                    answers_surfaces_list.append(s)
                    text_input.clear_text()
                    events = pygame.event.get()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            if click:
                if back_button.rectangle.collidepoint((mx, my)):
                    return correct

            # Feed it with events every frame
            text_input.update(events)

            screen.blit(bg, (0, 0))
            screen.blit(filter, rect_filter)
            screen.blit(pl_life_text, vida_text)
            screen.blit(pl_life, vida)
            screen.blit(title_img, title_rect)
            screen.blit(qSurface, qRect)
            for s in surfaces_list:
                screen.blit(*s)
            for s in answers_surfaces_list:
                screen.blit(*s)
            back_button.draw_button(screen)
            # print(len(answers_surfaces_list))

            # Blit its surface onto the screen
            if times_pressed == 0:
                screen.blit(text_input.get_surface(), (480, 230))
                answer_rect = (480,230)
            elif times_pressed == 1:
                screen.blit(text_input.get_surface(), (1045, 230))
                answer_rect = (1045, 230)
            elif times_pressed == 2:
                screen.blit(text_input.get_surface(), (480, 260))
                answer_rect = (480, 260)
            elif times_pressed == 3:
                screen.blit(text_input.get_surface(), (800, 260))
                answer_rect = (800, 260)
            elif times_pressed == 4:
                screen.blit(text_input.get_surface(), (240, 290))
                answer_rect = (240, 290)
            elif times_pressed == 5:
                screen.blit(text_input.get_surface(), (530, 290))
                answer_rect = (530, 290)
            elif times_pressed == 6:
                screen.blit(text_input.get_surface(), (875, 290))
                answer_rect = (875, 290)
            elif times_pressed == 7:
                answered = True
            pygame.display.update()

        if self.password_answer_correct(answers):
            correct = True
        else:
            player.life -= 10

        pygame.display.update()
        return correct

    def password_answer_correct(self, answers):
        isCorrect = False
        if answers[0] == self.airplane_n:
            if answers[1] == self.departure_time:
                if answers[2] == self.sigsauer_rifles:
                    if answers[3] == self.atomic_bombs:
                        if answers[4] == self.lmg_rifles :
                            if answers[5] == self.lmg_caliber:
                                if answers[6] == self.arrival_time:
                                    isCorrect = True
        return isCorrect