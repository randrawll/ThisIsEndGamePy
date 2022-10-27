import pygame

class Camera:
    def __init__(self, w, h):
        self.camera = pygame.Rect(0, 0, w, h)
        self.width = w
        self.height = h

    def apply(self, e):
        return e.rect.move(self.camera.topleft)

    def update(self, target, width, height):
        x = -target.rect.x + int(width / 2)
        y = -target.rect.y + int(height / 2)
        self.camera = pygame.Rect(x, y, self.width, self.height)