import pygame
pygame.init()

clock=pygame.time.Clock()

screen = pygame.display.set_mode()
#equilibrium position
x0=0
y0=0
#initial velocities
xdot0=10
ydot0=0

#Spring constants

x_spring = 1
y_spring = 1

size=50#the size of the mass but should be based on screen size insted
x_equilibrium = (pygame.display.get_surface().get_width()-size)/2
y_equilibrium = (pygame.display.get_surface().get_height()-size)/2
initial_position_x=x_equilibrium+x0
initial_position_y=y_equilibrium-y0
mass=pygame.Rect(initial_position_x, initial_position_y, size, size)
#inital position
screen.fill((255,255,255))
pygame.draw.rect(screen, (255, 0, 0), mass)
pygame.display.update()
#t=1 position
xdot=xdot0-(mass.x-x_equilibrium)*x_spring
ydot=ydot0-y_spring*(mass.y-y_equilibrium)
mass.x += xdot
mass.y -= ydot
screen.fill((255,255,255))
pygame.draw.rect(screen, (255, 0, 0), mass)
pygame.display.update()

run = True
while run:

    clock.tick(60)

    xdot -= x_spring*(mass.x-initial_position_x)
    mass.x += xdot
    mass.y -= ydot0#-y_spring*(mass.y-initial_position_y)
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (255, 0, 0), mass)
    print(mass.x,mass.y)
    print(xdot)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    pygame.display.update()

pygame.quit()#have a way to quit from in game?