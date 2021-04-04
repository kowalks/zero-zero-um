from screens import *
from buttons import *
class SettingScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    def run_events(self, running):
        mx, my = pygame.mouse.get_pos()
        back_button = buttons.Button(settings.MARGIN + 3 * settings.BT_DIST,
                                     settings.SCREEN_HEIGHT - settings.MARGIN,
                                     "Voltar", "blue_button")
        video_button = buttons.Button(settings.MARGIN,
                                      settings.MARGIN,
                                      "Vídeo", "blue_button")
        video_button.draw_button(self.scn)
        back_button.draw_button(self.scn)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        # TODO: Antes de dar push, organizar essa implementacao do quit button
        if back_button.rectangle.collidepoint((mx, my)):
            if click:
                title_screen = TitleScreen()
                running = title_screen.run(running)
        if video_button.rectangle.collidepoint((mx, my)):
            if click:
                video_setting_button_type1 = buttons.Button(settings.MARGIN + 2 * settings.BT_DIST,
                                     settings.SCREEN_HEIGHT - settings.MARGIN,
                                     "Restore default", "blue_button")

                video_setting_button_type1.draw_button(self.scn)
        return running