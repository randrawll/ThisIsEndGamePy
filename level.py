import pygame
from spritesheet import Spritesheet
from settings import *

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

    def drawgrid(self, screen):
        for x in range(0, SCREEN_WIDTH, TILESIZE):
            pygame.draw.line(screen, (200, 0, 0), (x, 0), (x, SCREEN_HEIGHT)) 
        for y in range(0, SCREEN_WIDTH, TILESIZE):
            pygame.draw.line(screen, (200, 0, 0), (0, y), (SCREEN_WIDTH, y)) 
        
class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.gameSprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE