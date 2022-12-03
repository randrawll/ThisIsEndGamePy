import pygame
import random
from settings import *
vector = pygame.math.Vector2

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h, enemytype):
        self.groups = game.gameSprites, game.enemies, game.obstacles
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        #self.image = pygame.Surface((16,16))
        #self.image.fill(RED)
        self.etype = enemytype
        if self.etype == "tideman":
            self.image = game.tidemanImage
        elif self.etype == "fly":
            self.image = game.flyImage
        self.rect = self.image.get_rect()
        self.vel = vector(0,0)
        self.pos = vector(x, y)
        self.hp = 3
        self.spawn_time = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.spawn_time > 100:
            self.move()
            self.spawn_time = pygame.time.get_ticks()
        #if pygame.sprite.spritecollideany(self, self.game.playerSprite):
        #    self.kill()
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

        #fun one
        # if pygame.time.get_ticks() - self.spawn_time > 1000:
        #     self.vel = self.game.player.pos - self.pos
        #     num = random.randrange(1,10)
        #     if num % 2 == 0:
        #         self.vel = E_MOVESPEED * self.vel.normalize()
        #     else:
        #         self.vel.y = E_MOVESPEED * random.randrange(-5,5)
        #         self.vel.x = E_MOVESPEED * random.randrange(-5,5)
        #     self.spawn_time = pygame.time.get_ticks()


 