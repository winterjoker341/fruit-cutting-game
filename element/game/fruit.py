import math
import random
import pygame

class Fruit(pygame.sprite.Sprite):
    def __init__(self, name, pos, size):
        super(Fruit, self).__init__()
        self.pos = pos
        self.size = size
        self.name = name

        self.angle = math.pi*49/100
        self.speed = 35
        self.time = 0
        self.gravity = 0.98

        self.rotate_angle = 0
        self.rotate_angle_weight = random.randint(1, 3)

        self.cuttable = True
 
        self.set_image(1)

    def set_image(self, key):
        self.surf = pygame.transform.scale(pygame.image.load(f"asset/fruits/{self.name}/{key}.png"), self.size)
        self.rect = self.surf.get_rect(center = self.pos)

    def rotate(self):
        self.surf_copy = pygame.transform.rotate(self.surf, self.rotate_angle)
        self.rotate_angle -= self.rotate_angle_weight
        self.rect = self.surf_copy.get_rect(center = self.pos)

    def update(self):
        self.pos[0] += self.speed*math.cos(self.angle)
        self.pos[1] -= self.speed*math.sin(self.angle)-self.gravity*self.time
        self.time += 1
        self.rotate()

    def draw(self, screen):
        screen.blit(self.surf_copy, self.rect)
