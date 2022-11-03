from tkinter import Y
import pygame
from os import path
from player import Player
from things import Things, Wall, Ground, Spritesheet
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
        self.img_folder = path.join(game_dir, 'img')
        self.map_folder = path.join(game_dir, 'maps')
        self.ground_sheet = Spritesheet("img/grass.png")
        self.map = Map(path.join(self.map_folder, 'map.txt'))

    def initialize(self):
        self.gameSprites = pygame.sprite.Group()
        self.ground = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.thing = Things()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                Ground(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)
    
    def run(self):
        self.running = True
        while self.running:
            self.dt = self.clock.tick(30) / 1000
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
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(NICEBLUE)
        self.ground.draw(self.screen)
        #self.thing.drawgrid(self.screen)
        for sprite in self.gameSprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pygame.display.flip()

g = Game()
g.initialize()
while True:
    g.run()
  





