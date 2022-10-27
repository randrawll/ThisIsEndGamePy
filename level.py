import pygame
from spritesheet import Spritesheet

class Level(pygame.sprite.Sprite):
    def __init__(self):
        super(Level, self)
        self.sheet = Spritesheet("grass.png")
        self.tiles = []
        self.rects = []
        for i in range(2):
            self.tiles.append(self.sheet.loadSheet((i * 32,0,32,32)))
            


    def draw(self, screen): 
        for x in range(10):
            for y in range(10):
                if x % 2 == 0:
                    screen.blit(self.tiles[0], (x * 32, y * 32))
                else:
                    screen.blit(self.tiles[1], (x * 32, y * 32))  
        
