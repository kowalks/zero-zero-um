import pygame
import settings

class Button():
    def __init__(self, x_pos, y_pos, bt_text = "", bt_img_name = ""):
        self.text = bt_text
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
                (int(settings.BT_WIDTH*1.1), settings.BT_HEIGHT))

    def draw_button(self, screen):
        Rect = self.button_img.get_rect()
        Rect.x = self.x
        Rect.y = self.y
        self.rectangle = Rect
        position = self.text_surface.get_rect(center = Rect.center)
        screen.blit(self.button_img, (self.x, self.y))
        screen.blit(self.text_surface, position)

class ButtonFight():
    def __init__(self, x_pos, y_pos, bt_text = "", bt_img_name = "", index = 0):
        self.index = index
        self.x = x_pos
        self.y = y_pos
        self.rectangle = pygame.Rect(x_pos, y_pos,
                                     settings.BT_WIDTH,
                                     settings.BT_HEIGHT)
        if bt_text != "":
            smallfont = pygame.font.Font(f'fonts/{settings.BT_FONT}.ttf', 15)
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
    def __init__(self, x_pos, y_pos, size, center, bt_img_name = "", item = 0):
        size = 0.6*size
        w, h = (int(size), int(size))
        self.x = x_pos
        self.y = y_pos
        self.rectangle = pygame.Rect(x_pos, y_pos,
                                     size,
                                     size)
        self.rectangle.center = center

        font = pygame.font.Font(f'fonts/{settings.BT_FONT}.ttf', 15)

        self.font = font

        self.item_number = font.render(str(item), True, settings.WHITE)
        self.item_rect = self.item_number.get_rect(center= (self.rectangle.bottomright[0]-2,self.rectangle.bottomright[1]-5))
        if bt_img_name != "":
            self.img_off= pygame.transform.scale(
                pygame.image.load(f'img/itens/black_white_{bt_img_name}.png'),
                (h, w))
            self.img_on = pygame.transform.scale(
                pygame.image.load(f'img/itens/{bt_img_name}.png'),
                (h, w))
            self.button_img = self.img_off
            print(bt_img_name)


    def draw_button(self, screen):
        screen.blit(self.button_img, self.rectangle)
        screen.blit(self.item_number, self.item_rect)

    def update(self, item,screen):
        self.item_number = self.font.render(str(item), True, settings.WHITE)
        if item == 0:
            self.button_img = self.img_off
        else:
            self.button_img = self.img_on
        self.draw_button(screen)
