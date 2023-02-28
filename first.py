import pygame
import random


clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((720, 360))
pygame.display.set_caption('Pygame_1')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('images/bg.jpg').convert()

ghost  = pygame.image.load('images/ghost.png').convert_alpha()
ghost_list = []

walk_left = [
    pygame.image.load('images/player_left/player_left_1.png').convert_alpha(),
    pygame.image.load('images/player_left/player_left_2.png').convert_alpha(),
    pygame.image.load('images/player_left/player_left_3.png').convert_alpha(),
    pygame.image.load('images/player_left/player_left_4.png').convert_alpha(),
    pygame.image.load('images/player_left/player_left_5.png').convert_alpha(),
    pygame.image.load('images/player_left/player_left_6.png').convert_alpha(),
    pygame.image.load('images/player_left/player_left_7.png').convert_alpha(),
    pygame.image.load('images/player_left/player_left_8.png').convert_alpha()]

walk_right = [
    pygame.image.load('images/player_right/player_right_1.png').convert_alpha(),
    pygame.image.load('images/player_right/player_right_2.png').convert_alpha(),
    pygame.image.load('images/player_right/player_right_3.png').convert_alpha(),
    pygame.image.load('images/player_right/player_right_4.png').convert_alpha(),
    pygame.image.load('images/player_right/player_right_5.png').convert_alpha(),
    pygame.image.load('images/player_right/player_right_6.png').convert_alpha(),
    pygame.image.load('images/player_right/player_right_7.png').convert_alpha(),
    pygame.image.load('images/player_right/player_right_8.png').convert_alpha()]

anim_player_count = 0
bg_x = 0

player_speed = 12
player_x = 100
player_y = 225

score = 0
top_score = score

jump = False
jump_count = 7

ghost_timer = pygame.USEREVENT + 1

gameplay = True

label = pygame.font.Font('data/Lato-Regular.ttf', 40)

start_label = label.render('GO!!!', False, (66, 189, 187))
start_label_rect = start_label.get_rect(topleft=(270, 150))
lose_label = label.render('You lose!', False, (193, 196, 199))
restart_label = label.render('restart', False, (115, 132, 148))
restart_label_rect = restart_label.get_rect(topleft=(285, 220))

bullet = pygame.image.load('images/wind.png').convert_alpha()
bullets = []
cd = 5
log = False
first_spawn = True
start = False
running = True
while running:
    if not start:
        screen.fill((186, 73, 65))
        screen.blit(start_label, start_label_rect)

        mouse = pygame.mouse.get_pos()
        if start_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            start = True
            score = 0
            player_x = 100
            ghost_list.clear()
            bullets.clear()

    else:
        if first_spawn:
            t = 300
            pygame.time.set_timer(ghost_timer, t)
            first_spawn = False
        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + 720, 0))

        if gameplay:
            player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
            score_label = label.render('Score: {0}'.format(score), False, 'black')
            top_score_label = label.render('TOP score : {0}'.format(top_score), False, 'black')
            screen.blit(score_label, (5, 5))
            screen.blit(top_score_label, (380, 5))

            if ghost_list:
                for (i, el) in enumerate(ghost_list):
                    screen.blit(ghost, el)
                    el.x -= 10

                    if el.x < -40:
                        ghost_list.pop(i)

                    if player_rect.colliderect(el):
                        gameplay = False

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
                if keys[pygame.K_UP]:
                    jump = True
            else:
                if jump_count >= -7:
                    if jump_count > 0:
                        player_y -= jump_count ** 2 / 2
                    else:
                        player_y += jump_count ** 2 / 2
                    jump_count -= 1
                else:
                    jump = False
                    jump_count = 7

            if anim_player_count == 7:
                anim_player_count = 0
            else:
                anim_player_count += 1

            bg_x -= 2
            if bg_x == -720:
                bg_x = 0



            if bullets:
                for (i, el) in enumerate(bullets):
                    screen.blit(bullet, (el.x, el.y))
                    el.x += 4

                    if el.x > 740:
                        bullets.pop(i)

                    if ghost_list:
                        for (index, ghost_el) in enumerate(ghost_list):
                            if el.colliderect(ghost_el):
                                ghost_list.pop(index)
                                bullets.pop(i)
                                score += 100
                                if score > top_score:
                                    top_score = score



        else:
            screen.fill((87, 88, 89))
            screen.blit(lose_label, (270, 150))
            screen.blit(restart_label, restart_label_rect)

            mouse = pygame.mouse.get_pos()
            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplay = True
                score = 0
                player_x = 100
                ghost_list.clear()
                bullets.clear()

    if cd > 0:
        cd -= 1
    if log:
        cd = 10
        log = False
    pygame.display.update()

    clock.tick(10)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_SPACE and cd == 0:
            bullets.append(bullet.get_rect(topleft=(player_x + 30, player_y + 10)))
            log = True
        if event.type == ghost_timer:
            if random.randrange(2) == 0:
                ghost_list.append(ghost.get_rect(topleft=(740, 240)))
            else:
                ghost_list.append(ghost.get_rect(topleft=(740, 195)))
            t = random.randint(300, 3000)
            pygame.time.set_timer(ghost_timer, t)
