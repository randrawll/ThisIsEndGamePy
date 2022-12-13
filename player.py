import pygame
from settings import *
from things import Weapon
vector = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.gameSprites, game.playerSprite
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.playerImageFront
        self.imageFront = game.playerImageFront
        self.imageBack = game.playerImageBack
        self.imageLeft = game.playerImageLeft
        self.imageRight = game.playerImageRight
        self.rect = self.image.get_rect()
        self.vel = vector(0,0)
        self.pos = vector(x, y)
        self.direction = {"Up": False, "Down": False, "Left": False, "Right": False}
        self.health = 10
        self.spawn_time = pygame.time.get_ticks()
        self.hittimer = 0
        self.doHit = False

    def update(self):
        self.move()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x 
        collide_wall(self, self.game.walls, "x")
        self.rect.y = self.pos.y 
        collide_wall(self, self.game.walls, "y")

        if pygame.sprite.spritecollideany(self, self.game.enemies) and pygame.time.get_ticks() - self.hittimer > 1000:
            self.hit()
        if self.health < 1:
            self.kill()
        self.doHit = False

    def hit(self):
        self.hittimer = pygame.time.get_ticks()
        self.health -= 1
        self.doHit = True
        self.hitimage = pygame.Surface((32,32))
        self.hitimage.fill(RED)
        self.hitrect = self.pos
        self.image = self.hitimage
        print(self.health)

    def draw(self, screen): 
        screen.blit(self.image, self.rect)

    def weapon(self, e):
        if e == K_SPACE:
             for k in self.direction:
                if self.direction[k]:
                    print(k)
                    Weapon(self.game, self.pos, k)

    def move(self):
        self.pressed = False
        self.vel = vector(0,0)
        self.klist = pygame.key.get_pressed()
        if self.klist[K_w] and self.pressed == False:
            self.pressed = True
            self.vel.y = -MOVESPEED
            self.image = self.imageBack
            self.rect = self.image.get_rect()
            self.direction = {"Up": False, "Down": False, "Left": False, "Right": False}
            self.direction["Up"] = True
        if self.klist[K_s] and self.pressed == False:
            self.pressed = True
            self.vel.y = MOVESPEED
            self.image = self.imageFront
            self.direction = {"Up": False, "Down": False, "Left": False, "Right": False}
            self.direction["Down"] = True
        if self.klist[K_a] and self.pressed == False:
            self.pressed = True
            self.vel.x = -MOVESPEED
            self.image = self.imageLeft
            self.direction = {"Up": False, "Down": False, "Left": False, "Right": False}
            self.direction["Left"] = True
        if self.klist[K_d] and self.pressed == False:
            self.pressed = True
            self.vel.x = MOVESPEED
            self.image = self.imageRight
            self.direction = {"Up": False, "Down": False, "Left": False, "Right": False}
            self.direction["Right"] = True
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071

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

def collide_enemy(sprite, group, direction):
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



 