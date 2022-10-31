import pygame
from settings import *
from pygame.locals import (K_UP,K_DOWN,K_LEFT,K_RIGHT,K_SPACE,K_ESCAPE,KEYDOWN,KEYUP,QUIT)

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.gameSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y

        #self.playerImage = pygame.image.load("duck.png").convert()
        #self.playerImage.set_colorkey((0, 0, 0))
        #self.rect = self.playerImage.get_rect()
    
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


    def draw(self, screen): 
        screen.blit(self.image, self.rect)
        #self.rect = self.playerImage.get_rect()
        #self.rect.move_ip(self.x, self.y)
        #screen.blit(self.playerImage, self.rect)

    def move(self, dt):
        self.klist = pygame.key.get_pressed()
        if pygame.key.get_pressed()[K_UP]:
            self.y += -1 * dt * TILESIZE
        if pygame.key.get_pressed()[K_DOWN]:
            self.y += dt * TILESIZE
        if pygame.key.get_pressed()[K_LEFT]:
            self.x += -1 * dt * TILESIZE
        if pygame.key.get_pressed()[K_RIGHT]:
            self.x += dt * TILESIZE
        #if pygame.key.get_pressed()[K_SPACE]:
        #    self.attack()

    def checkKeys(player):
        klist = pygame.key.get_pressed()
        if pygame.key.get_pressed()[K_UP]:
            player.y += MOVESPEED * -1
        if pygame.key.get_pressed()[K_DOWN]:
            player.y += MOVESPEED 
        if pygame.key.get_pressed()[K_LEFT]:
            player.x += MOVESPEED * -1
        if pygame.key.get_pressed()[K_RIGHT]:
            player.x += MOVESPEED
        if pygame.key.get_pressed()[K_SPACE]:
            player.attack()
        for e in pygame.event.get():
            #if e.type == pygame.KEYDOWN: 
            #if e.type == pygame.KEYUP:     return 0
            if e.type == pygame.QUIT: pygame.quit() 

    def checkBounds(thing):
        if thing.x > SCREEN_WIDTH - TILESIZE:   thing.x = SCREEN_WIDTH - TILESIZE - 1
        if thing.x < 0:                         thing.x = 1
        if thing.y > SCREEN_HEIGHT - TILESIZE:  thing.y = SCREEN_HEIGHT - TILESIZE - 1
        if thing.y < 0:                         thing.y = 1