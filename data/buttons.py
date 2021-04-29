import pygame
import settings

class Button():
    def __init__(self, x_pos, y_pos, bt_text = "", bt_img_name = ""):
        self.x = x_pos
        self.y = y_pos
        self.rectangle = pygame.Rect(x_pos, y_pos,
                                     settings.BT_WIDTH,
                                     settings.BT_HEIGHT)
        if bt_text != "":
            smallfont = pygame.font.Font(f'fonts/{settings.BT_FONT}.ttf', 30)
            self.text_surface = smallfont.render(bt_text, True, settings.WHITE)

        if bt_img_name != "":
            self.button_img = pygame.transform.scale(
                pygame.image.load(f'img/buttons/{bt_img_name}.png'),
                (settings.BT_WIDTH, settings.BT_HEIGHT))

    def draw_button(self, screen):
        width_text, height_text = self.text_surface.get_size()
        x_text_pos = self.x + settings.BT_WIDTH/2 - width_text/2
        y_text_pos = self.y + settings.BT_HEIGHT/2 - height_text/2
        screen.blit(self.button_img, (self.x, self.y))
        screen.blit(self.text_surface, (x_text_pos, y_text_pos))

class ButtonFight():
    def __init__(self, x_pos, y_pos, bt_text = "", bt_img_name = ""):
        self.x = x_pos
        self.y = y_pos
        self.rectangle = pygame.Rect(x_pos, y_pos,
                                     settings.BT_WIDTH,
                                     settings.BT_HEIGHT)
        if bt_text != "":
            smallfont = pygame.font.Font(f'fonts/{settings.BT_FONT}.ttf', 30)
            self.text_surface = smallfont.render(bt_text, True, settings.BLACK)

        if bt_img_name != "":
            self.button_img = pygame.transform.scale(
                pygame.image.load(f'img/buttons/{bt_img_name}.png'),
                (settings.BT_WIDTH, settings.BT_HEIGHT))

    def draw_button(self, screen):
        width_text, height_text = self.text_surface.get_size()
        x_text_pos = self.x + settings.BT_WIDTH/2 - width_text/2
        y_text_pos = self.y + settings.BT_HEIGHT/2 - height_text/2
        screen.blit(self.button_img, (self.x, self.y))
        screen.blit(self.text_surface, (x_text_pos, y_text_pos))

class ButtonItens():
    def __init__(self, x_pos, y_pos, w = settings.BT_WIDTH, h = settings.BT_HEIGHT, bt_text = "", bt_img_name = ""):
        self.x = x_pos
        self.y = y_pos
        self.rectangle = pygame.Rect(x_pos, y_pos,
                                     w,
                                     h)
        if bt_text != "":
            smallfont = pygame.font.Font(f'fonts/{settings.BT_FONT}.ttf', 30)
            self.text_surface = smallfont.render(bt_text, True, settings.BLACK)

        if bt_img_name != "":
            self.button_img = pygame.transform.scale(
                pygame.image.load(f'img/buttons/{bt_img_name}.png'),
                (settings.BT_WIDTH, settings.BT_HEIGHT))

    def draw_button(self, screen):
        width_text, height_text = self.text_surface.get_size()
        x_text_pos = self.x + settings.BT_WIDTH/2 - width_text/2
        y_text_pos = self.y + settings.BT_HEIGHT/2 - height_text/2
        screen.blit(self.button_img, (self.x, self.y))
        screen.blit(self.text_surface, (x_text_pos, y_text_pos))

