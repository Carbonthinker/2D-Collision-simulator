import pygame
import sys
from body import *
from space import Space

DIMENSIONS = (1080, 720)
FPS = 120

# BODIES
rec1 = Body(
            pos0 = [0,200], 
            dim = (100, 100), 
            color = (250, 0, 0), 
            mass = 30, 
            velocity = [10, 0])
rec2 = Body(
            pos0 = [620,200], 
            dim = (20, 20), 
            color = (0, 250, 0), 
            mass = 5, 
            velocity = [-2, 0])
rec3 = Body(
            pos0 = [610,250], 
            dim = (20, 20), 
            color = (0, 250, 0), 
            mass = 5, 
            velocity = [-2, 2])
bodies = (rec1, rec2, rec3)


pygame.init()
screen = pygame.display.set_mode(DIMENSIONS)
clock = pygame.time.Clock()
space = Space(DIMENSIONS, bodies)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    screen.fill("white")

    space.updatePos(1)
    bodies = space.getBodies()
    for obj in bodies:
        pygame.draw.rect(screen, obj[1], obj[0])

    pygame.display.flip()
    clock.tick(FPS)

