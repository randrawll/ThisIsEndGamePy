import pygame
from player import Player

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([SCREEN_WIDTH , SCREEN_HEIGHT])
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT,
)


running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False 
            if event.key == K_UP:
                player.y -= 10
            if event.key == K_DOWN:
                player.y += 10
            if event.key == K_LEFT:
                player.x -= 10
            if event.key == K_RIGHT:
                player.x += 10          
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    player.draw(screen)
    print("Player: " + str(player.x) + " " + str(player.y))

    pygame.display.flip()


pygame.quit()

