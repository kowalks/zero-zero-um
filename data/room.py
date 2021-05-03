from os import path
import pytmx

class TiledRoom:
    def __init__(self, filename):
        folder = path.dirname(__file__)
        tm = pytmx.load_pygame(path.join(folder,  f'map/{filename}.tmx'), pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self, surface, xRoom, yRoom):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth + self.width * xRoom,
                                            y *self.tmxdata.tileheight + self.height * yRoom))

    def make_room(self, rooms_surface, xRoom, yRoom):
        self.render(rooms_surface, xRoom, yRoom)
        return rooms_surface