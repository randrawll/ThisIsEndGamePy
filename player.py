import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self)
        self.x = x 
        self.y = y
        self.hp = 100
        self.playerImage = pygame.image.load("duck.png").convert()
        self.playerImage.set_colorkey((0, 0, 0))
        self.rect = self.playerImage.get_rect()

    def draw(self, screen): 
        self.rect = self.playerImage.get_rect()
        self.rect.move_ip(self.x, self.y)
        screen.blit(self.playerImage, self.rect)


