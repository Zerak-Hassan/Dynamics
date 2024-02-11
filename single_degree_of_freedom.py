import pygame
pygame.init()

screen = pygame.display.set_mode()
x0=100
y0=100
initial_position_x=pygame.display.get_surface().get_width()/2-25+x0
initial_position_y=pygame.display.get_surface().get_height()/2-25-y0
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