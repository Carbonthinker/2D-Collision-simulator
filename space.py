from body import Body

class Space:
    def __init__(self, dim, bodies):
        self.dim = dim
        self.bodies = bodies
    
    def updatePos(self, time):
        for obj in self.bodies:
            obj.pos0[0] += obj.velocity[0] * time
            obj.pos0[1] += obj.velocity[1] * time
        self.updateVel()
        self.updateColisions()
        

    
    def updateVel(self):
        for i in self.bodies:
            if i.pos0[0] < 0 or i.pos0[0] + i.dim[0] > self.dim[0]:
                i.velocity[0] = -i.velocity[0]

            if i.pos0[1] < 0 or i.pos0[1] + i.dim[1] > self.dim[1]:
                i.velocity[1] = -i.velocity[1]
            # With gravity
            """
            if i.pos0[1] < 0 or i.pos0[1] + i.dim[1] > self.dim[1]:
                i.velocity[1] = min(-(i.velocity[1] - 0.5 * i.mass), 0)
            else:
                i.velocity[1] += 9.81
            """
            
    
    def updateColisions(self):
        x_col_pairs = set()
        for i in self.bodies:
            for k in self.bodies:
                if i != k:
                    col = (i, k)
                    overlap_x = i.pos0[0] + i.dim[0] > k.pos0[0] and k.pos0[0] + k.dim[0] > i.pos0[0]
                    overlap_y = i.pos0[1] + i.dim[1] > k.pos0[1] and k.pos0[1] + k.dim[1] > i.pos0[1]
                    if overlap_x and overlap_y:
                        if (k, i) not in x_col_pairs:
                            x_col_pairs.add(col)
        
        for col in x_col_pairs:
            i = col[0]
            k = col[1]

            m1 = i.mass
            m2 = k.mass
            v1x = i.velocity[0]
            v2x = k.velocity[0]
            v1y = i.velocity[1]
            v2y = k.velocity[1]
            i.velocity[0] = ((m1 - m2) * v1x + 2 * m2 * v2x) / (m1 + m2)
            k.velocity[0] = ((m2 - m1) * v2x + 2 * m1 * v1x) / (m2 + m1)
            i.velocity[1] = ((m1 - m2) * v1y + 2 * m2 * v2y) / (m1 + m2)
            k.velocity[1] = ((m2 - m1) * v2y + 2 * m1 * v1y) / (m2 + m1)
    
    
    def getBodies(self):
        bodies = []
        for obj in self.bodies:
            bodies.append(obj.getObj())
        return bodies