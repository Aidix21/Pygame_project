import pygame


pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('Pygame_1')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('images/bg.png')

running = True
while running:
    screen.blit(bg, (-10, 0))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()