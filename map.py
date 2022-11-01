import pygame
from settings import *

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'r') as f:
            for line in f:
                self.data.append(line)
    
        self.mapwidth = len(self.data)
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

    def update(self, target):
        x = -target.rect.x + int(SCREEN_WIDTH / 2)
        y = -target.rect.y + int(SCREEN_HEIGHT / 2)
        #limit
        x = min(0, x)
        y = min(0, y)
        #x = max(-(self.width - SCREEN_WIDTH), x)  
        x = max(-(980), x)
        y = max(-(self.height - SCREEN_HEIGHT), y)
        print(str(x) + " : " + str(y))
        self.camera = pygame.Rect(x, y, self.width, self.height)
