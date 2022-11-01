import pygame
from pygame.sprite import Sprite
class Settings():
    def __init__(self):
        self.bullet_speed = 12
        self.bullet_weight = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.image = pygame.image.load('bullet.png')

class Bullet(Sprite):
    def __init__(self, aos):
        super().__init__()
        self.screen = aos.screen
        self.settings = Settings()
        self.color = self.settings.bullet_color
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect()

        self.rect = pygame.Rect(0, 0, self.settings.bullet_weight, self.settings.bullet_height)
        self.rect.midtop = aos.ship.rect.midtop
        self.y = float(self.rect.y)
    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)