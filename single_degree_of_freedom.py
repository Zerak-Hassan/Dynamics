import pygame
pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#get the screen resolution somehow
x0=0
y0=300
initial_position_x=(SCREEN_WIDTH/2)-50+x0
initial_position_y=(SCREEN_HEIGHT/2)-50-y0
mass=pygame.Rect(initial_position_x, initial_position_y, 50, 50)

run = True
while run:
    screen.fill((255,255,255))

    pygame.draw.rect(screen, (255, 0, 0), mass)#be able to have this rectangle move with some velocity

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    pygame.display.update()

pygame.quit()#have a way to quit from in game?