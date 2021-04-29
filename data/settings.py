import pygame
import sys

# Screen size settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Screen caption
CAPTION = "Zero-zero-um"

# Margins size
MARGIN = 15/128*SCREEN_WIDTH

# Buttons size and distances
BT_WIDTH = int(20/128*SCREEN_WIDTH)
BT_HEIGHT = int(SCREEN_HEIGHT/10)
BT_DIST =  BT_WIDTH + 6/128*SCREEN_WIDTH

# Fonts
BT_FONT = "SuperLegendBoy"

# Some colors RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
TITLE = "Zero Zero Um"
FPS = 30
BGCOLOR = DARKGREY

TILESIZE = 64
GRIDWIDTH = SCREEN_WIDTH / TILESIZE  # 40 in default
GRIDHEIGHT = SCREEN_HEIGHT / TILESIZE # 22.5 in default

PLAYER_SPEED = 20

ROOMSIZE = 16

MAPSIZE = 5 # in rooms


