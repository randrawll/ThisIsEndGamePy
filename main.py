import pygame
from player import Player
from level import Level
from settings import *
from pygame.locals import (K_UP,K_DOWN,K_LEFT,K_RIGHT,K_SPACE,K_ESCAPE,KEYDOWN,KEYUP,QUIT)

moveSpeed = 1

class Game():
    def __init__(self):  
        pygame.init()
        self.screen = pygame.display.set_mode([SCREEN_WIDTH , SCREEN_HEIGHT])
        self.clock = pygame.time.Clock()

    def initialize(self):
        self.gameSprites = pygame.sprite.Group()
        self.player = Player(self, 10, 10)
        self.level = Level(SCREEN_WIDTH, SCREEN_HEIGHT)
    
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
        self.player.move(dt)
        self.gameSprites.update()

    def draw(self):
        self.screen.fill((0,0,0))
        self.level.drawgrid(self.screen)
        self.gameSprites.draw(self.screen)
        pygame.display.flip()


    
#player.draw(screen)
#pygame.display.update()
    
g = Game()
g.initialize()
while True:
    g.run()
  





