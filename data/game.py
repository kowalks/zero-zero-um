import pygame

class Game:
    """ Main class for the state of the game """

    running = True

    def __init__(self):
        pygame.init()


    def close(self):
        pygame.quit()