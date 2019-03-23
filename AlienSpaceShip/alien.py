import pygame
import  random

class Alien(pygame.sprite.Sprite):
    def __init__(self,ai_settings, screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        level=2
        image_name = 'images/alien%d.png' %level
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 初始化时外星飞船的位置
        self.rect.x = random.randint(self.screen_rect.left,self.screen_rect.right-self.rect.width)
        self.rect.y = 0
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        # self.trackx()
        self.y += self.ai_settings.aliens_speedy
        self.rect.top = self.y

    def trackx(self):

        # speedx= self.ai_settings.aliens_speedx
        if self.rect.right >= self.screen_rect.right:
            self.ai_settings.aliens_speedx= -1*self.ai_settings.aliens_speedx
        if self.rect.left <= self.screen_rect.left:
            self.ai_settings.aliens_speedx= -1*self.ai_settings.aliens_speedx
            # self.x +=  self.ai_settings.aliens_speedx
        self.x += self.ai_settings.aliens_speedx
        self.rect.x = self.x
        # print('rectx= ' + str(self.rect.x))




