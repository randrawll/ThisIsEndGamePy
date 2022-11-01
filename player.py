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
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE

    def update(self):
        self.move()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x 
        self.collide('x')
        self.rect.y = self.y 
        self.collide('y')

    def draw(self, screen): 
        screen.blit(self.image, self.rect)

    def move(self):
        self.vx, self.vy = 0, 0
        self.klist = pygame.key.get_pressed()
        if self.klist[K_UP] or self.klist[K_w] :
            self.vy = -MOVESPEED
        if self.klist[K_DOWN] or self.klist[K_s]:
            self.vy = MOVESPEED
        if self.klist[K_LEFT] or self.klist[K_a]:
            self.vx = -MOVESPEED
        if self.klist[K_RIGHT] or self.klist[K_d]:
            self.vx = MOVESPEED
        #if self.klist[K_SPACE]:
        #    self.attack()
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071


    def collide(self, d):
        if d == "x":
            xhit = pygame.sprite.spritecollide(self, self.game.walls, False)
            if xhit:
                if self.vx > 0:
                    self.x = xhit[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = xhit[0].rect.right
            self.vx = 0
            self.rect.x = self.x
        if d == "y":
            yhit = pygame.sprite.spritecollide(self, self.game.walls, False)
            if yhit:
                if self.vy > 0:
                    self.y = yhit[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = yhit[0].rect.bottom
            self.vy = 0
            self.rect.y = self.y


 