import sys
import pygame, bullet, alien
import time


def game_control(ai_ship, ai_settings, screen, bullet_group, alien_group,state,play_botton):
    """生成外星飞船"""
    if len(alien_group) == 0:
        # time.sleep(3)
        generate_alien(ai_settings, screen, alien_group)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_events(event, ai_ship, ai_settings, screen, bullet_group)
        elif event.type == pygame.KEYUP:
            keyup_events(event, ai_ship)
        elif event.type == pygame.MOUSEBUTTONUP:
            mousex,mousey = pygame.mouse.get_pos()
            check_play_botton(state,play_botton,mousex,mousey)

def check_play_botton(state,play_botton,mousex,mousey):
    if play_botton.rect.collidepoint(mousex,mousey):
        state.game_active = True
        play_botton.is_active =False
        pygame.mouse.set_visible(False)


def fire_bullet(ai_settings, screen, ai_ship, bullet_group):
    """开火，产生子弹"""
    if len(bullet_group) < ai_settings.bullet_limit:
        bullets = bullet.Bullet(ai_settings, screen, ai_ship)
        bullet_group.add(bullets)
        # del_bullet(bullet_group)


def bullet_update(bullet_group,alien_group):
    """删除子弹"""
    bullet_group.update()
    for bull in bullet_group:
        if bull.rect.bottom <= 0:
            bullet_group.remove(bull)


def alien_update(bullet_group,alien_group,screen,gamestate,play_botton):
    # generate_alien(ai_settings,screen,alien_group)
    alien_group.update()
    alien_destroyed(bullet_group, alien_group)
    for aliens in alien_group:
            if alien_invade(aliens,screen) :
                gamestate.game_life -=1
                if gamestate.game_life<=0:
                    gamestate.game_active = False
                    play_botton.is_active = True
                    pygame.mouse.set_visible(True)
                    gamestate.reset()
                alien_group.remove(aliens)

def alien_invade(aliens,screen):
    return aliens.rect.bottom >= screen.get_rect().bottom


def alien_destroyed(bullet_group,alien_group):
    # 返回值collisions为字典类型,碰撞后两者同时消失
    collisions = pygame.sprite.groupcollide(bullet_group,alien_group,True,True)

def generate_alien(ai_settings, screen, alien_group):
    if len(alien_group) < ai_settings.aliens_numlimit:
        new_alien = alien.Alien(ai_settings, screen)
        alien_group.add(new_alien)

# def ship_update():


def update_screen(ai_settings, screen, ai_ship, bullet_group, alien_group,play_button):
    screen.fill(ai_settings.bgcolor)
    for alien in alien_group.sprites():
        alien.blitme()
    for bull in bullet_group.sprites():
        bull.bullet_show()
    ai_ship.blitme()
    if play_button.is_active:
        play_button.draw_button()
    pygame.display.flip()


def keydown_events(event, ai_ship, ai_settings, screen, bullet_group):
    if event.key == pygame.K_RIGHT:
        ai_ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ai_ship.moving_left = True
    elif event.key == pygame.K_UP:
        ai_ship.moving_front = True
    elif event.key == pygame.K_DOWN:
        ai_ship.moving_backward = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ai_ship, bullet_group)


def keyup_events(event, ai_ship):
    if event.key == pygame.K_RIGHT:
        ai_ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ai_ship.moving_left = False
    elif event.key == pygame.K_UP:
        ai_ship.moving_front = False
    elif event.key == pygame.K_DOWN:
        ai_ship.moving_backward = False
