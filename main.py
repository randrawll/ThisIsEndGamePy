from tkinter import Y
import pygame
from os import path
from player import Player
from enemy import Enemy
from things import Things, Spritesheet, Obstacle, Weapon
from map import Map, Camera, TiledMap
from settings import *

class Game():
    def __init__(self):  
        pygame.init()
        self.screen = pygame.display.set_mode([SCREEN_WIDTH , SCREEN_HEIGHT])
        self.clock = pygame.time.Clock()
        self.load()

    def load(self):
        self.map = TiledMap(path.join(MAP_FOLDER, 'tiled1.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.playerImage = pygame.image.load(path.join(IMG_FOLDER, 'duck.png')).convert_alpha()

    def initialize(self, mapNum):
        self.thing = Things()
        self.gameSprites = pygame.sprite.Group()
        self.playerSprite = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.weapons = pygame.sprite.Group()
        
        for objects in self.map.tmxdata.objects:
            if objects.name == "player":
                self.player = Player(self, objects.x, objects.y)
            if objects.name == "enemy1":
                Enemy(self, objects.x, objects.y, objects.width, objects.height)
            if objects.name == "wall":
                Obstacle(self, objects.x, objects.y, objects.width, objects.height)

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
            if e.type == pygame.KEYDOWN:
                if e.key == K_SPACE:
                    #self.initialize(2)
                    Weapon(self, self.player.pos, "x")

    def update(self):
        self.gameSprites.update()
        self.camera.update(self.player)

    def draw(self):
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        #self.thing.drawgrid(self.screen)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.gameSprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pygame.display.flip()

g = Game()
g.initialize(1)
while True:
    g.run()





