import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.gameSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.image.load("duck.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y
        self.name = "TEST"

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def draw(self, screen): 
        screen.blit(self.image, self.rect)

    def move(self, dt):
        self.klist = pygame.key.get_pressed()
        if pygame.key.get_pressed()[K_UP] or pygame.key.get_pressed()[K_w] :
            self.y += -1 * dt * MOVESPEED
        if pygame.key.get_pressed()[K_DOWN] or pygame.key.get_pressed()[K_s]:
            self.y += dt * MOVESPEED
        if pygame.key.get_pressed()[K_LEFT] or pygame.key.get_pressed()[K_a]:
            self.x += -1 * dt * MOVESPEED 
        if pygame.key.get_pressed()[K_RIGHT] or pygame.key.get_pressed()[K_d]:
            self.x += dt * MOVESPEED
        #if pygame.key.get_pressed()[K_SPACE]:
        #    self.attack()


    def checkBounds(thing):
        if thing.x > SCREEN_WIDTH - TILESIZE:   thing.x = SCREEN_WIDTH - TILESIZE - 1
        if thing.x < 0:                         thing.x = 1
        if thing.y > SCREEN_HEIGHT - TILESIZE:  thing.y = SCREEN_HEIGHT - TILESIZE - 1
        if thing.y < 0:                         thing.y = 1