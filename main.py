import sys
import  pygame
from objects import Bullet
class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('background.jpg')
        self.rect = self.image.get_rect()
class Ship():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("ship3.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right:
            self.rect.x += 10
    def update2(self):
        if self.moving_left:
            self.rect.x -= 10
    def light(self):
        self.screen.blit(self.image, self.rect)
class Settings():
    def __init__(self):
        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (0, 0, 0)
class Testgame:
    def __init__(self):

        pygame.init()
        self.settings = Settings()
        pygame.display.set_caption('Никита')
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        self.bullet = pygame.sprite.Group()
        self.bulet = Bullet(self)
    def rungame(self):
        while True:
            self._update_screen()
            self.ship.update()
            self.ship.update2()
            self._check_events()
            self.bullet.update()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                elif event.key == pygame.K_SPACE:
                    self._firebullet()
                elif event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
    def _firebullet(self):
        new_bullet = Bullet(self)
        self.bullet.add(new_bullet)
    def _update_screen(self):
        self.background = Background()
        self.screen.blit(self.bulet.image, self.bulet.rect)
        self.screen.blit(self.background.image, self.background.rect)
        self.ship.light()
        for bullet in self.bullet.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
if __name__ == '__main__':
    tg = Testgame()
    tg.rungame()