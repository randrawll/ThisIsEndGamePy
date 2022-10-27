import pygame
from player import Player
from level import Level
from camera import Camera
from pygame.locals import (K_UP,K_DOWN,K_LEFT,K_RIGHT,K_SPACE,K_ESCAPE,KEYDOWN,KEYUP,QUIT)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILESIZE = 32
moveSpeed = 10


def main():
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH , SCREEN_HEIGHT])
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    level = Level(SCREEN_WIDTH, SCREEN_HEIGHT)
    running = True
    x_velo, y_velo = 0, 0
    clock = pygame.time.Clock()
    cam = Camera(SCREEN_WIDTH * 2, SCREEN_HEIGHT * 2)

    while running:
        screen.fill((0, 0, 0))

        checkKeys(player) 
        #checkBounds(player)

        level.draw(screen)
        player.draw(screen)

        cam.update(player, SCREEN_WIDTH * 2, SCREEN_HEIGHT * 2)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(30)

def checkKeys(player):
    klist = pygame.key.get_pressed()
    if pygame.key.get_pressed()[K_UP]:
        player.y += moveSpeed * -1
    if pygame.key.get_pressed()[K_DOWN]:
        player.y += moveSpeed 
    if pygame.key.get_pressed()[K_LEFT]:
        player.x += moveSpeed * -1
    if pygame.key.get_pressed()[K_RIGHT]:
        player.x += moveSpeed
    if pygame.key.get_pressed()[K_SPACE]:
        player.attack()
    for e in pygame.event.get():
        #if e.type == pygame.KEYDOWN: 
        #if e.type == pygame.KEYUP:     return 0
        if e.type == pygame.QUIT: pygame.quit()   

def checkBounds(thing):
    if thing.x > SCREEN_WIDTH - TILESIZE:   thing.x = SCREEN_WIDTH - TILESIZE - 1
    if thing.x < 0:                         thing.x = 1
    if thing.y > SCREEN_HEIGHT - TILESIZE:  thing.y = SCREEN_HEIGHT - TILESIZE - 1
    if thing.y < 0:                         thing.y = 1

main()




