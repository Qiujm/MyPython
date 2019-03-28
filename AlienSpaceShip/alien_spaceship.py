# import sys
import pygame
import settings, ship, button, game_state
import game_functions as gf


# print(settings.screen_width)
# print(settings.screen_height)
def run_game():
    pygame.init()
    ai_settings = settings.Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("AlienSpaceShip")
    alien_group = pygame.sprite.Group()

    bullet_group = pygame.sprite.Group()
    ai_ship = ship.Ship(ai_settings, screen)
    # ai_ship = pygame.sprite.Group()
    state = game_state.Gamestate(ai_settings, bullet_group, alien_group)
    play_button = button.Button(ai_settings, screen, 'Play', state)

    while True:
        gf.game_control(ai_ship, ai_settings, screen, bullet_group, alien_group, state, play_button)
        if state.game_active:
            ai_ship.update()
            gf.alien_update(bullet_group, alien_group, screen, state, play_button)
            gf.bullet_update(bullet_group, alien_group)
        gf.update_screen(ai_settings, screen, ai_ship, bullet_group, alien_group, play_button)

run_game()
