import pygame
from element.base.text import Text

class Rank(pygame.sprite.Sprite):
    def __init__(self, grade, score, pos, size, color):
        self.pos = pos
        self.color = color

        self.grade = Text(f"# {grade}", (size[1]//2, size[1]//2), 30, (0, 0, 255))
        self.score = Text(f"{score}", ((size[0]+size[1])//2, size[1]//2), 30, (0, 0, 255))

        self.surf = pygame.Surface(size)
        self.surf.fill(self.color)
        self.grade.draw(self.surf)
        self.score.draw(self.surf)
        self.rect = self.surf.get_rect(center = self.pos)
    
    def draw(self, screen):
        screen.blit(self.surf, self.rect)