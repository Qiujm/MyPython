import pygame

class Gamestate():
    game_active=False
    game_life = 1
    score = 0
    def __init__(self,ai_settings,bullet_group,alien_group):
        self.ai_settings = ai_settings
        self.bullet_group = bullet_group
        self.alien_group = alien_group
        self.reset()
        # self.game_active=True

    def reset(self):
        self.bullet_group.empty()
        self.alien_group.empty()

        self.game_active = False
        self.game_life = 1





