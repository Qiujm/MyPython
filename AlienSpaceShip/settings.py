class Settings():
    # screen_width = 0
    # screen_height = 0

    def __init__(self):
        # screen parameters
        self.screen_width = 900
        self.screen_height = 600
        self.bgcolor = (230, 230, 230)

        self.ship_speed = 0.8

        # bullet settings
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255,0,0)
        self.bullet_limit = 10
        # self.bullet_speed = 1.5
        # print(type(self.bullet_color))

        self.aliens_speedx = 1.0
        self.aliens_speedy = 0.25
        self.aliens_numlimit = 10


