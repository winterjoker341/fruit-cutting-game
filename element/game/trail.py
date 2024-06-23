import pygame

class Trail:
    def __init__(self, color, width):
        self.width = width
        self.color = color
        self._particles = []
    
    def add(self, pos):
        self._particles.append(Point(pos))

    def update(self):
        for particle in self._particles:
            particle.update()
            if particle.time<=0:
                self._particles.remove(particle)

    def draw(self, screen):
        for i in range(len(self._particles)-1):
            pygame.draw.line(screen, self.color, self._particles[i].pos, self._particles[i+1].pos, self.width)

class Point:
    def __init__(self, pos):
        self.pos = pos
        self.time = 10

    def update(self):
        self.time -= 1
