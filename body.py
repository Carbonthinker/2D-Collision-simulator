import pygame

class Body:
    def __init__(self, pos0, dim, color, mass, velocity):
        self.pos0 = pos0
        self.dim = dim
        self.color = color
        self.mass = mass
        self.velocity = velocity
    
    def getObj(self):
        object = pygame.Rect(self.pos0[0], self.pos0[1], self.dim[0], self.dim[1])
        return (object, self.color)


