import pygame

class Body:
    def __init__(self, screen, pos0, dim, color, mass, velocity):
        self.screen = screen
        self.pos0 = pos0
        self.dim = dim
        self.object = pygame.Rect(pos0[0], pos0[1], dim[0], dim[1]),
        self.color = color
        self.mass = mass
        self.velocity = velocity
    
    def updatePos(self, time):
        new_x = self.pos0[0] + self.velocity[0] * time
        new_y = self.pos0[1] + self.velocity[1] * time
        if new_x < 0 or new_x + self.dim[0] > self.screen.get_size()[0]:
            new_x = self.pos0[0]
            self.velocity[0] = 0
        if new_y < 0 or new_y + self.dim[1] > self.screen.get_size()[1]:
            new_y = self.pos0[1]
            self.velocity[1] = 0

        self.pos0 = (new_x, new_y)
        self.object = pygame.Rect(self.pos0[0], self.pos0[1], self.dim[0], self.dim[1]),