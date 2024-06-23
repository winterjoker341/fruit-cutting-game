import pygame

class Button:
    def __init__(self, pos, size, color):
        self.color = color
        self.rect = pygame.Rect(pos, size)
    
    def isCollised(self, point):
        return self.rect.collidepoint(point)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)