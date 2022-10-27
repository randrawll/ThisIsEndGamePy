import pygame
from player import Player
from level import Level
from pygame.locals import (K_UP,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,KEYDOWN,KEYUP,QUIT)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILESIZE = 32
moveSpeed = 10


def main():
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH , SCREEN_HEIGHT])
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    level = Level()
    running = True
    x_velo, y_velo = 0, 0
    clock = pygame.time.Clock()

    while running:
        screen.fill((0, 0, 0))

        keyPressed = checkKeys()  
        if keyPressed == K_UP:       y_velo = moveSpeed * -1
        elif keyPressed == K_DOWN:   y_velo = moveSpeed
        elif keyPressed == K_LEFT:   x_velo = moveSpeed * -1
        elif keyPressed == K_RIGHT:  x_velo = moveSpeed
        elif keyPressed == 0:        x_velo, y_velo = 0, 0

        player.x += x_velo
        player.y += y_velo

        checkBounds(player)
        
        level.draw(screen)
        player.draw(screen)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(30)
        print(keyPressed)

def checkKeys():
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:   return e.key
        if e.type == pygame.KEYUP:     return 0
        if e.type == pygame.QUIT: pygame.quit()   

def checkBounds(thing):
    if thing.x > SCREEN_WIDTH - TILESIZE:   thing.x = SCREEN_WIDTH - TILESIZE - 1
    if thing.x < 0:                         thing.x = 1
    if thing.y > SCREEN_HEIGHT - TILESIZE:  thing.y = SCREEN_HEIGHT - TILESIZE - 1
    if thing.y < 0:                         thing.y = 1


#def printInfo():
    #print("Player: " + str(player.x) + " " + str(player.y))
    #print("SCREEN: " + str(SCREEN_WIDTH) + " " + str(SCREEN_HEIGHT))

main()




