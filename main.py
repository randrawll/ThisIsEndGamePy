from tkinter import Y
import pygame
from os import path
from player import Player
from enemy import Enemy
from things import Things, Spritesheet, Obstacle, Weapon, HealthBar
from map import Map, Camera, TiledMap
from settings import *
vector = pygame.math.Vector2

class Game():
    def __init__(self):  
        pygame.init()
        self.screen = pygame.display.set_mode([SCREEN_WIDTH , SCREEN_HEIGHT])
        self.clock = pygame.time.Clock()
        self.finalLevel = 3
        self.levelCounter = 1
        self.startgame = True
        self.load(self.levelCounter)

    def load(self, mapnum):
        if mapnum == 1:
            self.map = TiledMap(path.join(MAP_FOLDER, 'endgame_map1.tmx'))
            self.enemycount = 1
        elif mapnum == 2:
            self.map = TiledMap(path.join(MAP_FOLDER, 'endgame_map2.tmx'))
            self.enemycount = 1
        elif mapnum == 3:
            self.map = TiledMap(path.join(MAP_FOLDER, 'endgame_map3.tmx'))
            self.enemycount = 1
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()

        self.playerImageFront = pygame.image.load(path.join(IMG_FOLDER, 'duck.png')).convert_alpha()
        self.playerImageBack = pygame.image.load(path.join(IMG_FOLDER, 'duck_back.png')).convert_alpha()
        self.playerImageLeft = pygame.image.load(path.join(IMG_FOLDER, 'duck_left.png')).convert_alpha()
        self.playerImageRight = pygame.image.load(path.join(IMG_FOLDER, 'duck_right.png')).convert_alpha()
        self.sprayImage = pygame.image.load(path.join(IMG_FOLDER, 'spray.png')).convert_alpha()
        self.flyImage = pygame.image.load(path.join(IMG_FOLDER, 'fly.png')).convert_alpha()
        self.tidemanImage = pygame.image.load(path.join(IMG_FOLDER, 'tideman.png')).convert_alpha()
        self.tickImage = pygame.image.load(path.join(IMG_FOLDER, 'tick.png')).convert_alpha()

    def initialize(self, pausedstate):
        self.paused = pausedstate
        self.thing = Things()
        self.gameSprites = pygame.sprite.Group()
        self.playerSprite = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.weapons = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.health = pygame.sprite.Group()
        self.healthbar = HealthBar(self)
        
        for objects in self.map.tmxdata.objects:
            if objects.name == "wall":
                Obstacle(self, objects.x, objects.y, objects.width, objects.height)
            if objects.name == "player":
                self.player = Player(self, objects.x, objects.y)
            if objects.name == "enemy1":
                Enemy(self, objects.x, objects.y, objects.width, objects.height, "fly")
            if objects.name == "enemy2":
                Enemy(self, objects.x, objects.y, objects.width, objects.height, "tick")
            if objects.name == "enemy3":
                Enemy(self, objects.x, objects.y, objects.width, objects.height, "tideman")

        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        self.running = True
        self.startgame = True
        while self.running:
            self.dt = self.clock.tick(30) / 1000
            if self.paused or self.levelCounter == self.finalLevel + 1:
                self.events()
                #self.draw()
                self.menu()
            else:
                self.events()
                self.update()
                self.draw()

    def events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT: pygame.quit() 
            if e.type == pygame.KEYDOWN:
                if e.key == K_ESCAPE:
                    if self.paused:
                        self.paused = False
                    else:
                        self.paused = True
                elif e.key == K_SPACE:
                    self.player.weapon(e.key)
                    
    def update(self):
        self.gameSprites.update()
        self.camera.update(self.player)

        if self.enemycount == 0:
            self.levelCounter += 1
            self.load(self.levelCounter)
            self.initialize(False)

    def draw(self):
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        #self.thing.drawgrid(self.screen)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.gameSprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        #self.screen.blit(self.healthbar.image, self.camera.apply(self.healthbar))
        pygame.display.flip()

    def menu(self):
        self.menuimage = pygame.image.load(path.join(IMG_FOLDER, 'menu.png')).convert_alpha()
        self.menuimage = pygame.transform.scale(self.menuimage, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.menurect = self.menuimage.get_rect()
        self.screen.blit(self.menuimage, self.menurect)
        pygame.display.flip()

g = Game()
g.initialize(True)
while True:
    g.run()





