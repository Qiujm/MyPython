import pygame


class Ship(pygame.sprite.Sprite):
    # moving_right = False
    # moving_left = False
    # moving_front = False
    # moving_backward = False

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.moving_left = False
        self.moving_right = False
        self.moving_front = False
        self.moving_backward = False
        self.ai_settings = ai_settings
        self.screen = screen
        # 加载图像并获取其外接矩形
        self.image = pygame.image.load('images/spaceship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将飞船初始化在底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.bottom)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ai_settings.ship_speed
            self.rect.centerx = self.x
            # print('x=' + str(self.x) + ',type x = ' + str(type(self.x)))
            # print('centerx=' + str(self.rect.centerx) + ',type centerx = ' + str(type(self.rect.centerx)))
        if self.moving_left and self.rect.left > 0:
            self.x -= self.ai_settings.ship_speed
            self.rect.centerx = self.x
        if self.moving_front and self.rect.top > 0:
            self.y -= self.ai_settings.ship_speed
            self.rect.bottom=self.y
        if self.moving_backward and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.ai_settings.ship_speed
            self.rect.bottom = self.y
