import math
import random
import pygame

class Splash:
    def __init__(self, pos, size, name):
        self.angle = random.random()%math.pi
        self.angle_list = [
            math.degrees(2*math.pi-self.angle),
            math.degrees(2*math.pi-self.angle),
            math.degrees(2*math.pi-self.angle)
        ]
        self.pos_list = [
            pos,
            self.rotation_matrix(pos, 50, -50),
            self.rotation_matrix(pos, -50, 50)
        ]
        self.size = size
        self.time = 200

        self.surf_list = []
        self.rect_list = []

        for num in range(1, 4):
            img = pygame.image.load(f"asset/splash/{name}/{num}.png")
            surf = pygame.transform.rotate(pygame.transform.scale(img, self.size), self.angle_list[num-1])
            rect = surf.get_rect(center = self.pos_list[num-1])
            self.surf_list.append(surf)
            self.rect_list.append(rect)

    def rotation_matrix(self, pos, x, y):
        xp = pos[0]+x*math.cos(self.angle)-y*math.sin(self.angle)
        yp = pos[1]+x*math.sin(self.angle)+y*math.cos(self.angle)
        return [xp, yp]

    def update(self):
        self.time -= 1

    def draw(self, screen):
        for i in range(3):
            screen.blit(self.surf_list[i], self.rect_list[i])