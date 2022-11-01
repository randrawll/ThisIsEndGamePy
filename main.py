from tkinter import Y
import pygame
from player import Player
from level import Level, Wall
from settings import *

prev_x = 0
prev_y = 0

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
            Wall(self, x, 5)
    
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
        if not collide(self.player, self.walls):
            self.player.move(dt)
        self.gameSprites.update()

    def draw(self):
        self.screen.fill((0,0,0))
        self.level.drawgrid(self.screen)
        self.gameSprites.draw(self.screen)
        pygame.display.flip()

def collide(player, group):
    if pygame.sprite.spritecollideany(player, group): 
        player.x = prev_x
        player.y = prev_y
        return True
    prev_x = player.x
    prev_y = player.y
    return False

g = Game()
g.initialize()
while True:
    g.run()
  





