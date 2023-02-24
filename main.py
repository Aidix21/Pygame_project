import pygame


pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Pygame_1')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
color = (51, 193, 212)
screen.fill(color)

square = pygame.Surface((50, 170))
square.fill('blue')

myfont = pygame.font.Font('fonts/Lato-Regular.ttf', 40)
text_surface = myfont.render('Pygame', False, 'white')

player = pygame.image.load('images/icon.png')

running = True
while running:
    screen.blit(square, (10, 10))
    pygame.draw.circle(screen, 'red', (300, 150), 40)
    screen.blit(text_surface, (300, 50))
    screen.blit(player, (300, 1))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                if color == (51, 193, 212):
                    color = (209, 51, 212)
                else:
                    color = (51, 193, 212)
                screen.fill(color)

