import pygame.font


class Button():
    is_active = True
    def __init__(self,ai_settings,screen,msg,game_state):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 50, 10
        self.button_color = (255, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None,48)
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        self.game_state = game_state
        self.prep_msg(msg)
        # self.is_active = True

    def check_active(self):
        if self.game_state.game_active :
            self.is_active = False


    def set_active(self):
        self.is_active = True
        self.game_state.game_active = False

    def prep_msg(self,msg):
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)

    # def set_active(self):




