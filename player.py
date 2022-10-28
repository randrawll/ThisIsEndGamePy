import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self)
        self.x = x 
        self.y = y
        self.hp = 100
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

        #self.playerImage = pygame.image.load("duck.png").convert()
        #self.playerImage.set_colorkey((0, 0, 0))
        #self.rect = self.playerImage.get_rect()

    def draw(self, screen): 
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
        screen.blit(self.image, self.rect)
        #self.rect = self.playerImage.get_rect()
        #self.rect.move_ip(self.x, self.y)
        #screen.blit(self.playerImage, self.rect)


