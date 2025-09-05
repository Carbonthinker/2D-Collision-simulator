import pygame
import sys
from body import *
from space import Space

DIMENSIONS = (720, 1080)
FPS = 120

# BODIES
rec1 = Body(
            pos0 = [0,0], 
            dim = (100, 100), 
            color = (250, 0, 0), 
            mass = 30, 
            velocity = [2, 3])
rec2 = Body(
            pos0 = [500,600], 
            dim = (100, 100), 
            color = (0, 250, 0), 
            mass = 30, 
            velocity = [2, 0])
bodies = (rec1, rec2)


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

