import pygame
# from pygame.sprite import Sprite
# 1.实现子弹的定义和显示


class Bullet(pygame.sprite.Sprite):
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.rect = pygame.Rect(ship.rect.centerx, ship.rect.top, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.bottom)

    def update(self):
        self.y -= self.ai_settings.bullet_speed_factor
        self.rect.bottom = self.y
        # print('left=' + str(self.rect.left) + ',type x = ' + str(type(self.rect.left)))
        # print('right=' + str(self.rect.right) + ',type x = ' + str(type(self.rect.right)))
        # print('top=' + str(self.rect.top) + ',type x = ' + str(type(self.rect.top)))
        # print('bottom=' + str(self.rect.bottom) + ',type x = ' + str(type(self.rect.bottom)))

    def bullet_show(self):
        pygame.draw.rect(self.screen, self.ai_settings.bullet_color, self.rect)

# class Bullet(pygame.sprite.Sprite):
#     def __init__(self, ai_settings, screen, ship):
#         super(Bullet, self).__init__()
#         self.ai_settings = ai_settings
#         self.screen = screen
#         x = ship.rect.centerx
#         y = ship.rect.top
#         self.rect = pygame.Rect(x, y, ai_settings.bullet_width, ai_settings.bullet_height)  # test是否需要在参数前加self？
#         self.rect.centerx = x
#         self.rect.top = y
#         self.y = float(self.rect.y)
#
#     def bullet_show(self):
#         pygame.draw.rect(self.screen, self.ai_settings.bullet_color, self.rect)
#
#     def bullet_update(self):
#         # if self.rect.top > 0:
#         #     self.rect.top -= self.ai_settings.bullet_speed
#         self.y -= self.ai_settings.bullet_speed
#         self.rect.y = self.y
