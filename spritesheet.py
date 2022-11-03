import pygame

class Spritesheet(object):
    def __init__(self, path):
        self.spritesheet = pygame.image.load(path)
    
    #coords = (x, y, width, height)
    def loadSheet(self, tile):
        rect = pygame.Rect(tile)
        image = pygame.Surface(rect.size).convert_alpha()
        image.blit(self.spritesheet, (0,0), rect)
        return image
