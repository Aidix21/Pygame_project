import pygame


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pygame_1')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('images/bg.png')
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

running = True
while running:
    screen.blit(bg, (-10, 0))
    screen.blit(walk_right[anim_player_count], (150, 450))

    if anim_player_count == 7:
        anim_player_count = 0
    else:
        anim_player_count += 1

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()