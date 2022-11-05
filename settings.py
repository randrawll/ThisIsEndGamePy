import pygame
from os import path
from pygame.locals import (K_a, K_s, K_d, K_w, K_UP,K_DOWN,K_LEFT,K_RIGHT,K_SPACE,K_ESCAPE,KEYDOWN,KEYUP,QUIT)

GAME_DIR = path.dirname(__file__)
IMG_FOLDER = path.join(GAME_DIR, 'img')
MAP_FOLDER = path.join(GAME_DIR, 'maps')

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
TILESIZE = 32

MOVESPEED = 300
E_MOVESPEED = 100

#colors

NICEBLUE = (77, 132, 219)
NICEORANGE = (191, 144, 67)
GREEN = (166, 255, 107)
RED = (255, 0, 107)
BLACK = (0, 0, 0)

