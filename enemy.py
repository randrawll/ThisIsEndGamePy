import pygame
import random
from settings import *
from things import Bullet
vector = pygame.math.Vector2

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h, enemytype):
        self.groups = game.gameSprites, game.enemies, game.obstacles
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.etype = enemytype
        if self.etype == "tideman":
            self.hp = 50
            self.image = game.tidemanImage
        elif self.etype == "fly":
            self.hp = 3
            self.image = game.flyImage
        elif self.etype == "tick":
            self.hp = 10
            self.image = game.tickImage
        self.rect = self.image.get_rect()
        self.vel = vector(0,0)
        self.pos = vector(x, y)

        self.spawn_time = pygame.time.get_ticks()
        self.bullet_time = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.bullet_time > 2000:
            self.weapon()
            self.bullet_time = pygame.time.get_ticks()
        if pygame.time.get_ticks() - self.spawn_time > 100:
            self.move()
            self.spawn_time = pygame.time.get_ticks()
            self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x 
        self.rect.y = self.pos.y 

    def weapon(self):
        if self.etype == "tideman":
            Bullet(self.game, self.pos, "follow")
        if self.etype == "fly":
            Bullet(self.game, self.pos, "direction")

    def move(self):
        if self.etype == "tick":
            self.vel = self.game.player.pos - self.pos
            self.vel = BULLET_SPEED * self.vel.normalize()
            self.pos += self.vel * self.game.dt
            self.rect.center = self.pos
            self.vel.y = BULLET_SPEED * random.randrange(-5,5)
            self.vel.x = BULLET_SPEED * random.randrange(-5,5)
        else:
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


def collide_wall(sprite, group, direction):
    if direction == "x":
        xhit = pygame.sprite.spritecollide(sprite, group, False)
        if xhit:
            if sprite.vel.x > 0:
                sprite.pos.x = xhit[0].rect.left - sprite.rect.width
            if sprite.vel.x < 0:
                sprite.pos.x = xhit[0].rect.right
        sprite.vel.x = 0
        sprite.rect.x = sprite.pos.x
    if direction == "y":
        yhit = pygame.sprite.spritecollide(sprite, group, False)
        if yhit:
            if sprite.vel.y > 0:
                sprite.pos.y = yhit[0].rect.top - sprite.rect.height
            if sprite.vel.y < 0:
                sprite.pos.y = yhit[0].rect.bottom
        sprite.vel.y = 0
        sprite.rect.y = sprite.pos.y