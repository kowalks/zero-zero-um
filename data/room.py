import pygame
from os import path
import wall

class Room:
    def __init__(self, room_name):
        folder = path.dirname(__file__)
        self.room_data = []
        with open(path.join(folder, f'rooms/{room_name}.txt'), 'rt') as f:
            for line in f:
                self.room_data.append(line)


    def generate_walls(self, all_sprites, wall_sprites, x_room, y_room):
        for row, tiles in enumerate(self.room_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    wall.Wall(all_sprites, wall_sprites, x_room + col, y_room + row)