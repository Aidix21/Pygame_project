import pygame


clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((720, 360))
pygame.display.set_caption('Pygame_1')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('images/bg.jpg')
walk_left = [
    pygame.image.load('images/player_left/player_left_1.png'),
    pygame.image.load('images/player_left/player_left_2.png'),
    pygame.image.load('images/player_left/player_left_3.png'),
    pygame.image.load('images/player_left/player_left_4.png'),
    pygame.image.load('images/player_left/player_left_5.png'),
    pygame.image.load('images/player_left/player_left_6.png'),
    pygame.image.load('images/player_left/player_left_7.png'),
    pygame.image.load('images/player_left/player_left_8.png')]

walk_right = [
    pygame.image.load('images/player_right/player_right_1.png'),
    pygame.image.load('images/player_right/player_right_2.png'),
    pygame.image.load('images/player_right/player_right_3.png'),
    pygame.image.load('images/player_right/player_right_4.png'),
    pygame.image.load('images/player_right/player_right_5.png'),
    pygame.image.load('images/player_right/player_right_6.png'),
    pygame.image.load('images/player_right/player_right_7.png'),
    pygame.image.load('images/player_right/player_right_8.png')]

anim_player_count = 0
bg_x = 0

player_speed = 20
player_x = 100
player_y = 225

jump = False
jump_count = 6


running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 720, 0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[anim_player_count], (player_x, player_y))
    else:
        screen.blit(walk_right[anim_player_count], (player_x, player_y))

    if keys[pygame.K_LEFT] and player_x > 20:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 680:
        player_x += player_speed

    if not jump:
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if jump_count >= -6:
            if jump_count > 0:
                player_y -= jump_count ** 2 / 2
            else:
                player_y += jump_count ** 2 / 2
            jump_count -= 1
        else:
            jump = False
            jump_count = 6

    if anim_player_count == 7:
        anim_player_count = 0
    else:
        anim_player_count += 1

    bg_x -= 2
    if bg_x == -720:
        bg_x = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(10)