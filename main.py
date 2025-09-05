import pygame
import sys
from body import *

pygame.init()

screen = pygame.display.set_mode((720, 1080))

clock = pygame.time.Clock()

FPS = 120

rec1 = Body(
            screen = screen,
            pos0 = (0,0), 
            dim = (100, 100), 
            color = (250, 0, 0), 
            mass = 30, 
            velocity = (2, 3))
rec2 = Body(
            screen = screen,
            pos0 = (500,600), 
            dim = (100, 100), 
            color = (0, 250, 0), 
            mass = 30, 
            velocity = (2, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    rec1.updatePos(1)
    rec2.updatePos(1)

    screen.fill("white")
    pygame.draw.rect(screen, rec1.color, rec1.object)
    pygame.draw.rect(screen, rec2.color, rec2.object)

    pygame.display.flip()
    clock.tick(FPS)

