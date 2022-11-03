import pygame
from settings import *
vector = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.gameSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.image.load("img/duck.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.vel = vector(0,0)
        self.pos = vector(x, y) * TILESIZE

    def update(self):
        self.move()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x 
        self.collide('x')
        self.rect.y = self.pos.y 
        self.collide('y')

    def draw(self, screen): 
        screen.blit(self.image, self.rect)

    def move(self):
        self.vel = vector(0,0)
        self.klist = pygame.key.get_pressed()
        if self.klist[K_UP] or self.klist[K_w] :
            self.vel.y = -MOVESPEED
        if self.klist[K_DOWN] or self.klist[K_s]:
            self.vel.y = MOVESPEED
        if self.klist[K_LEFT] or self.klist[K_a]:
            self.vel.x = -MOVESPEED
        if self.klist[K_RIGHT] or self.klist[K_d]:
            self.vel.x = MOVESPEED
        #if self.klist[K_SPACE]:
        #    self.attack()
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071


    def collide(self, d):
        if d == "x":
            xhit = pygame.sprite.spritecollide(self, self.game.walls, False)
            if xhit:
                if self.vel.x > 0:
                    self.pos.x = xhit[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = xhit[0].rect.right
            self.vel.x = 0
            self.rect.x = self.pos.x
        if d == "y":
            yhit = pygame.sprite.spritecollide(self, self.game.walls, False)
            if yhit:
                if self.vel.y > 0:
                    self.pos.y = yhit[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = yhit[0].rect.bottom
            self.vel.y = 0
            self.rect.y = self.pos.y


 