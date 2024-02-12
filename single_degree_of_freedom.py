import pygame
pygame.init()

clock=pygame.time.Clock()

screen = pygame.display.set_mode()
#initial displacements
x0=0
y0=0
#initial velocities
xdot0=0
ydot0=1

size=50#needs to be set based on screen size insted 
initial_position_x=(pygame.display.get_surface().get_width()-size)/2+x0
initial_position_y=(pygame.display.get_surface().get_height()-size)/2-y0
mass=pygame.Rect(initial_position_x, initial_position_y, size, size)

screen.fill((255,255,255))
pygame.draw.rect(screen, (255, 0, 0), mass)
pygame.display.update()

run = True
while run:

    clock.tick(1)

    mass.x += xdot0
    mass.y -= ydot0
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (255, 0, 0), mass)
    print(mass.x)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    pygame.display.update()

pygame.quit()#have a way to quit from in game?