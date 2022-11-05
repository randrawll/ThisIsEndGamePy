import pygame
#from spritesheet import Spritesheet
from settings import *
import random

class Things(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def drawgrid(self, screen):
        for x in range(0, SCREEN_WIDTH, TILESIZE):
            pygame.draw.line(screen, (200, 0, 0), (x, 0), (x, SCREEN_HEIGHT)) 
        for y in range(0, SCREEN_WIDTH, TILESIZE):
            pygame.draw.line(screen, (200, 0, 0), (0, y), (SCREEN_WIDTH, y)) 

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(x, y, w, h)
        self.x = x 
        self.y = y
        self.rect.x = x 
        self.rect.y = y 

class Spritesheet(object):
    def __init__(self, path):
        self.spritesheet = pygame.image.load(path)

    def loadSheet(self, tile):
        rect = pygame.Rect(tile)
        image = pygame.Surface(rect.size).convert_alpha()
        image.blit(self.spritesheet, (0,0), rect)
        return image