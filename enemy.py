import pygame
import random
from settings import *
vector = pygame.math.Vector2

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.gameSprites, game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((16,16))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.vel = vector(0,0)
        self.pos = vector(x, y)

    def update(self):
        self.move()
        if pygame.sprite.spritecollideany(self, self.game.playerSprite):
            #self.game.player.kill()
            self.kill()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x 
        self.rect.y = self.pos.y 

    def move(self):
        self.vel = self.game.player.pos - self.pos
        num = random.randrange(1,10)
        if num % 2 == 0:
            self.vel = E_MOVESPEED * self.vel.normalize()
        else:
            self.vel.y = E_MOVESPEED * random.randrange(-5,5)
            self.vel.x = E_MOVESPEED * random.randrange(-5,5)


 