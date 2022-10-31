from tkinter import Y
import pygame
from player import Player
from level import Level, Wall
from settings import *



class Game():
    def __init__(self):  
        pygame.init()
        self.screen = pygame.display.set_mode([SCREEN_WIDTH , SCREEN_HEIGHT])
        self.clock = pygame.time.Clock()

    def initialize(self):
        self.gameSprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.player = Player(self, 2, 2)
        self.level = Level(SCREEN_WIDTH, SCREEN_HEIGHT)
        for x in range(10, 20):
            Wall(self, 10, 5)
    
    def run(self):
        self.running = True
        while self.running:
            self.dt = self.clock.tick(60) / 1000
            self.events()
            self.update(self.dt)
            self.draw()

    def events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT: pygame.quit() 

    def update(self, dt):
        if collide(self.player, self.walls):
            print("COLLIDE!")
        self.player.move(dt)
        self.gameSprites.update()

    def draw(self):
        self.screen.fill((0,0,0))
        self.level.drawgrid(self.screen)
        self.gameSprites.draw(self.screen)
        pygame.display.flip()


def collide(entity, group):
    for thing in group:
        if entity.x >= thing.x or entity.x <= thing.x + TILESIZE and entity.y >= thing.y or entity.y <= thing.y + TILESIZE:
        #if pygame.sprite.spritecollideany(entity, thing):    
            print(str(thing.x) + " : " + str(thing.y))
            print(str(entity.x) + " : " + str(entity.y))
            return True
    return False

g = Game()
g.initialize()
while True:
    g.run()
  





