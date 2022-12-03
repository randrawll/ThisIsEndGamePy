from tkinter import Y
import pygame
from os import path
from player import Player
from enemy import Enemy
from things import Things, Spritesheet, Obstacle, Weapon
from map import Map, Camera, TiledMap
from settings import *
vector = pygame.math.Vector2

class Game():
    def __init__(self):  
        pygame.init()
        self.screen = pygame.display.set_mode([SCREEN_WIDTH , SCREEN_HEIGHT])
        self.clock = pygame.time.Clock()
        self.load()

    def load(self):
        self.map1 = TiledMap(path.join(MAP_FOLDER, 'map1.tmx'))
        self.map2 = TiledMap(path.join(MAP_FOLDER, 'map2.tmx'))
        self.map_img = self.map1.make_map()
        self.map_rect = self.map_img.get_rect()
        self.playerImageFront = pygame.image.load(path.join(IMG_FOLDER, 'duck.png')).convert_alpha()
        self.playerImageBack = pygame.image.load(path.join(IMG_FOLDER, 'duck_back.png')).convert_alpha()
        self.playerImageLeft = pygame.image.load(path.join(IMG_FOLDER, 'duck_left.png')).convert_alpha()
        self.playerImageRight = pygame.image.load(path.join(IMG_FOLDER, 'duck_right.png')).convert_alpha()
        self.flyImage = pygame.image.load(path.join(IMG_FOLDER, 'fly.png')).convert_alpha()
        self.tidemanImage = pygame.image.load(path.join(IMG_FOLDER, 'tideman1.png')).convert_alpha()
        self.menuimage = pygame.image.load(path.join(IMG_FOLDER, 'menu.png'))
        self.menurect = self.menuimage.get_rect()

    def initialize(self, mapname):
        self.menu_on = True
        self.thing = Things()
        self.gameSprites = pygame.sprite.Group()
        self.playerSprite = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.weapons = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        
        for objects in self.map1.tmxdata.objects:
            if objects.name == "player":
                self.player = Player(self, objects.x, objects.y)
            if objects.name == "enemy1":
                Enemy(self, objects.x, objects.y, objects.width, objects.height)
            if objects.name == "wall":
                Obstacle(self, objects.x, objects.y, objects.width, objects.height)

        self.camera = Camera(self.map1.width, self.map1.height)

    def run(self):
        self.running = True
        while self.running:
            if self.menu_on:
                self.events()
                self.menu()
            else:
                self.dt = self.clock.tick(30) / 1000
                self.events()
                self.update()
                self.draw()

    def events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT: pygame.quit() 
            if e.type == pygame.KEYDOWN:
                if e.key == K_ESCAPE:
                    if self.menu_on:
                        self.initialize(1)
                        self.menu_on = False
                    else:
                        self.menu_on = True
                else:
                    self.player.weapon(e.key)
                    
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

    def menu(self):
        self.screen.blit(self.menuimage, self.menurect)
        pygame.display.flip()

g = Game()
g.initialize(1)
while True:
    g.run()





