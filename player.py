import pygame

class Player:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 25)

