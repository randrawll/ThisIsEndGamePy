import pygame
from settings import *
from things import Weapon
vector = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.gameSprites, game.playerSprite
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.playerImage
        self.rect = self.image.get_rect()
        self.vel = vector(0,0)
        self.pos = vector(x, y)

    def update(self):
        self.move()
        #self.weapon()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x 
        collide_wall(self, self.game.walls, "x")
        self.rect.y = self.pos.y 
        collide_wall(self, self.game.walls, "y")

    def draw(self, screen): 
        screen.blit(self.image, self.rect)

    # def weapon(self):
    #      for e in pygame.event.get():
    #          if e.type == pygame.KEYDOWN:
    #              if e.key == K_SPACE:
    #                  Weapon(self, self.pos, "x")

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
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071


def collide_wall(sprite, group, dir):
    if dir == "x":
        xhit = pygame.sprite.spritecollide(sprite, group, False)
        if xhit:
            if sprite.vel.x > 0:
                sprite.pos.x = xhit[0].rect.left - sprite.rect.width
            if sprite.vel.x < 0:
                sprite.pos.x = xhit[0].rect.right
        sprite.vel.x = 0
        sprite.rect.x = sprite.pos.x
    if dir == "y":
        yhit = pygame.sprite.spritecollide(sprite, group, False)
        if yhit:
            if sprite.vel.y > 0:
                sprite.pos.y = yhit[0].rect.top - sprite.rect.height
            if sprite.vel.y < 0:
                sprite.pos.y = yhit[0].rect.bottom
        sprite.vel.y = 0
        sprite.rect.y = sprite.pos.y

def collide_enemy(sprite, group, dir):
    if dir == "x":
        xhit = pygame.sprite.spritecollide(sprite, group, False)
        if xhit:
            if sprite.vel.x > 0:
                sprite.pos.x = xhit[0].rect.left - sprite.rect.width
            if sprite.vel.x < 0:
                sprite.pos.x = xhit[0].rect.right
        sprite.vel.x = 0
        sprite.rect.x = sprite.pos.x
    if dir == "y":
        yhit = pygame.sprite.spritecollide(sprite, group, False)
        if yhit:
            if sprite.vel.y > 0:
                sprite.pos.y = yhit[0].rect.top - sprite.rect.height
            if sprite.vel.y < 0:
                sprite.pos.y = yhit[0].rect.bottom
        sprite.vel.y = 0
        sprite.rect.y = sprite.pos.y



 