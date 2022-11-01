from tkinter import Y
import pygame
from os import path
from player import Player
from level import Level, Wall
from map import Map, Camera
from settings import *


class Game():
    def __init__(self):  
        pygame.init()
        self.screen = pygame.display.set_mode([SCREEN_WIDTH , SCREEN_HEIGHT])
        self.clock = pygame.time.Clock()
        self.load()

    def load(self):
        game_dir = path.dirname(__file__)
        self.map = Map(path.join(game_dir, 'map.txt'))


    def initialize(self):
        self.gameSprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.level = Level(SCREEN_WIDTH, SCREEN_HEIGHT)
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)
        
    
    def run(self):
        self.running = True
        while self.running:
            self.dt = self.clock.tick(60) / 1000
            self.events()
            self.update()
            self.draw()

    def events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT: pygame.quit() 

    def update(self):
        self.gameSprites.update()
        self.camera.update(self.player)

    def draw(self):
        self.screen.fill((0,0,0))
        #self.level.drawgrid(self.screen)
        for sprite in self.gameSprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pygame.display.flip()

g = Game()
g.initialize()
while True:
    g.run()
  





