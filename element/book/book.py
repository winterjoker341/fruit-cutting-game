import pygame

class Book:
    def __init__(self, pos, size, color):
        self.pos = pos
        self.size = size

        self.surf = pygame.Surface(self.size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect(center = self.pos)
    
    def set_image(self, name):
        self.surf = pygame.transform.scale(pygame.image.load(f"asset/fruits/{name}/1.png"), self.size)
        self.rect = self.surf.get_rect(center = self.pos)

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
