import pygame
from spritesheet import Spritesheet

TILESIZE = 32

class Level(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Level, self)
        self.width = width * 2
        self.height = height * 2
        self.sheet = Spritesheet("grass.png")
        self.tiles = []
        for i in range(2):
            self.tiles.append(self.sheet.loadSheet((i * TILESIZE,0,TILESIZE,TILESIZE)))
            
    def draw(self, screen): 
        for x in range(0, int(self.width / TILESIZE) + 1):
            for y in range(0, int(self.height / TILESIZE) + 1):
                if x % 2 == 0:
                    screen.blit(self.tiles[0], (x * TILESIZE, y * TILESIZE))
                else:
                    screen.blit(self.tiles[1], (x * TILESIZE, y * TILESIZE))  
        
