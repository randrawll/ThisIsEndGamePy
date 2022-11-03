import pygame
from spritesheet import Spritesheet
from settings import *
import random

class Things(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def draw(self, screen): 
        for x in range(0, int(self.width / TILESIZE) + 1):
            for y in range(0, int(self.height / TILESIZE) + 1):
                if x % 2 == 0:
                    screen.blit(self.tiles[0], (x * TILESIZE, y * TILESIZE))
                else:
                    screen.blit(self.tiles[1], (x * TILESIZE, y * TILESIZE))  

    def drawgrid(self, screen):
        for x in range(0, SCREEN_WIDTH, TILESIZE):
            pygame.draw.line(screen, (200, 0, 0), (x, 0), (x, SCREEN_HEIGHT)) 
        for y in range(0, SCREEN_WIDTH, TILESIZE):
            pygame.draw.line(screen, (200, 0, 0), (0, y), (SCREEN_WIDTH, y)) 

class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.ground
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.sheet = Spritesheet("img/grass.png")
        self.image = self.sheet.loadSheet((0,0,TILESIZE,TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = x
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.gameSprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.sheet = Spritesheet("img/ground.png")
        #self.tiles = []
        #for i in range(2):
        #    self.tiles.append(self.sheet.loadSheet((i * TILESIZE,0,TILESIZE,TILESIZE)))
        #self.image = self.tiles[0]
        self.image = self.sheet.loadSheet((0,0,TILESIZE,TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Spritesheet(object):
    def __init__(self, path):
        self.spritesheet = pygame.image.load(path)
    
    #coords = (x, y, width, height)
    def loadSheet(self, tile):
        rect = pygame.Rect(tile)
        image = pygame.Surface(rect.size).convert_alpha()
        image.blit(self.spritesheet, (0,0), rect)
        return image