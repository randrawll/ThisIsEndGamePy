import pygame
from settings import *
import random
vector = pygame.math.Vector2

class Things(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def drawgrid(self, screen):
        for x in range(0, SCREEN_WIDTH, TILESIZE):
            pygame.draw.line(screen, (200, 0, 0), (x, 0), (x, SCREEN_HEIGHT)) 
        for y in range(0, SCREEN_WIDTH, TILESIZE):
            pygame.draw.line(screen, (200, 0, 0), (0, y), (SCREEN_WIDTH, y)) 

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls, game.obstacles
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(x, y, w, h)
        self.x = x 
        self.y = y
        self.rect.x = x 
        self.rect.y = y 


# class HealthBar(pygame.sprite.Sprite):
#     def __init__(self, game):
#         self.groups = game.gameSprites, game.health
#         pygame.sprite.Sprite.__init__(self, self.groups)
#         self.game = game
#         self.image = pygame.Surface((100,15))
#         self.image.fill(RED)
#         self.rect = self.image.get_rect()

#     def update(self):
#         self.image = pygame.Surface((self.game.player.health * 20,15))
#         self.image.fill(RED)
#         self.rect.x = self.game.player.pos.x - 480
#         self.rect.y = self.game.player.pos.y - 380
    
#     def draw(self):
#         self.game.screen.blit(self.image, self.camera.apply(self))

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.gameSprites, game.health
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((100,5))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def update(self):
        self.image = pygame.Surface((self.game.player.health * 10,3))
        self.image.fill(RED)
        self.rect.x = self.game.player.pos.x - 30
        self.rect.y = self.game.player.pos.y + 40

    


class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, pos, bullettype):
        self.groups = game.gameSprites, game.bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.bullettype = bullettype
        self.image = pygame.Surface((10,10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.pos = vector(pos)
        self.rect.center = vector(pos)
        self.spawn_time = pygame.time.get_ticks()
        self.hittimer = 0
        self.vel = self.game.player.pos - self.pos
        self.vel = E_MOVESPEED * self.vel.normalize()

    def update(self):
        #follow player
        if self.bullettype == "follow":
            self.vel = self.game.player.pos - self.pos
            self.vel = BULLET_SPEED * self.vel.normalize()
            self.pos += self.vel * self.game.dt
            self.rect.center = self.pos
        if self.bullettype == "direction":
            self.pos += self.vel * self.game.dt
            self.rect.center = self.pos

        if pygame.sprite.spritecollideany(self, self.game.playerSprite):
            if pygame.time.get_ticks() - self.hittimer > 1000:
                self.hittimer = pygame.time.get_ticks()
                self.game.player.hit()
            self.kill()
        if pygame.sprite.spritecollideany(self, self.game.walls):
            self.kill()

class Weapon(pygame.sprite.Sprite):
    def __init__(self, game, pos, d):
        self.groups = game.gameSprites, game.weapons
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.image = game.sprayImage
        self.rect = self.image.get_rect()

        self.pos = vector(pos)
        self.rect.center = vector(game.player.pos.x - 16, game.player.pos.y + 16)
        self.vel = vector(0,0)
        self.dir = d
        self.spawn_time = pygame.time.get_ticks()

    def update(self):
        if pygame.sprite.spritecollideany(self, self.game.obstacles):
            self.kill()
            #print("HIT!")
        enemies = []
        enemy = pygame.sprite.spritecollideany(self, self.game.enemies)
        if enemy != None:
            #print(enemy.hp)
            enemy.hp -= 1
            if enemy.hp < 1:
                self.game.enemycount -= 1
                #print("enemy count: " + str(self.game.enemycount))
                enemy.kill()
        if pygame.time.get_ticks() - self.spawn_time > 1000:
            self.kill()
        if self.dir == "Left":
            self.vel.x = -MOVESPEED
        if self.dir == "Right":
            self.vel.x = MOVESPEED
        if self.dir == "Up":
            self.vel.y = -MOVESPEED
        if self.dir == "Down":
            self.vel.y = MOVESPEED
        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos


class Spritesheet(object):
    def __init__(self, path):
        self.spritesheet = pygame.image.load(path)

    def loadSheet(self, tile):
        rect = pygame.Rect(tile)
        image = pygame.Surface(rect.size).convert_alpha()
        image.blit(self.spritesheet, (0,0), rect)
        return image