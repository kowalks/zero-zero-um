import pygame
from os import path
import wall
import pytmx
import os


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

class TiledRoom:
    def __init__(self, filename):
        folder = path.dirname(__file__)
        tm = pytmx.load_pygame(path.join(folder,  f'map\{filename}.tmx'), pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y *self.tmxdata.tileheight))

    def make_room(self, rooms_surface):
        self.render(rooms_surface)
        return rooms_surface