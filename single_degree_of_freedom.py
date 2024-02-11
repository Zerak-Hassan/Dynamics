import pygame
pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
mass=pygame.Rect((SCREEN_WIDTH/2)-50, (SCREEN_HEIGHT/2)-50, 50, 50)

run = True
while run:
    screen.fill((255,255,255))

    pygame.draw.rect(screen, (255, 0, 0), mass)#be able to have this rectangle move with some velocity

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    pygame.display.update()

pygame.quit()