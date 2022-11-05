import pygame
import pytmx
from settings import *

class TiledMap:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))

    def make_map(self):
        temp_surface = pygame.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'r') as f:
            for line in f:
                self.data.append(line) 
        self.mapwidth = len(self.data[0])
        self.mapheight = len(self.data)
        self.width = self.mapwidth * TILESIZE
        self.height = self.mapheight * TILESIZE

class Camera:
    def __init__(self, w, h):
        self.camera = pygame.Rect(0, 0, w, h)
        self.width = w
        self.height = h 

    def apply(self, e):
        return e.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)


    def update(self, target):
        x = -target.rect.x + int(SCREEN_WIDTH / 2)
        y = -target.rect.y + int(SCREEN_HEIGHT / 2)
        x, y = min(0, x), min(0, y)
        x = max(-(self.width - (SCREEN_WIDTH + TILESIZE)), x)  
        y = max(-(self.height - SCREEN_HEIGHT), y)
        self.camera = pygame.Rect(x, y, self.width, self.height)
