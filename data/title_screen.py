import pygame
import settings

def title_screen():
    #Initialize pygame
    pygame.init()

    #Initialize screen and load background
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    bg = pygame.transform.scale(settings.TITLE_BG, (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

    #Initialize caption
    pygame.display.set_caption(settings.CAPTION)

    #Pygame screen load
    running = True
    while running:
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
