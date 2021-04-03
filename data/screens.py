import pygame
import settings
import buttons
import map

class Screen():
    """ Class of a generic screen in the game """
    def __init__(self, caption = "My game name", *args, **kwargs):
        # Initialize screen
        self.scn = pygame.display.set_mode((settings.SCREEN_WIDTH,
                                               settings.SCREEN_HEIGHT))
        # Load default background
        self.bg = pygame.transform.scale( # TODO: remove this when all bg defined
            pygame.image.load("img/background/bg_NONE.png"),
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
                running = game_screen.run(running)
        if controls_button.rectangle.collidepoint((mx, my)):
            if click:
                controls_screen = ControlsScreen()
                running = controls_screen.run(running)
        if settings_button.rectangle.collidepoint((mx, my)):
            if click:
                setting_screen = SettingsScreen()
                running = setting_screen.run(running)
        if quit_button.rectangle.collidepoint((mx, my)):
            if click:
                running = False

        return running

class SettingsScreen(Screen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run_events(self, running):

        mx, my = pygame.mouse.get_pos()

        quit_button = pygame.Rect(settings.MARGIN + 3*settings.BT_DIST,
                               settings.SCREEN_HEIGHT-settings.MARGIN,
                               settings.BT_WIDTH,
                               settings.BT_HEIGHT)

        pygame.draw.rect(self.scn, (49, 146, 179), quit_button)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if quit_button.collidepoint((mx, my)):
            if click:
                running = False

        return running

class ControlsScreen(Screen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run_events(self, running):

        mx, my = pygame.mouse.get_pos()

        quit_button = pygame.Rect(settings.MARGIN + 3*settings.BT_DIST,
                               settings.SCREEN_HEIGHT-settings.MARGIN,
                               settings.BT_WIDTH,
                               settings.BT_HEIGHT)

        pygame.draw.rect(self.scn, (49, 146, 179), quit_button)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if quit_button.collidepoint((mx, my)):
            if click:
                running = False

        return running

class GameScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run_events(self, running):
        game_map = map.Map()
        running = game_map.run(self.scn, running)
        return running