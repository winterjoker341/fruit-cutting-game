import pygame

class Text:
    def __init__(self, text, pos, size, color):
        self.pos = pos
        self.text = text
        self.color = color
        self.font = pygame.font.SysFont(None, size, True, True)
        self.set_text()

    def set_text(self):
        self.text = self.font.render(self.text, False, self.color)
        self.rect = self.text.get_rect(center=self.pos)

    def update(self, text):
        self.text = text
        self.set_text()

    def draw(self, screen):
        screen.blit(self.text, self.rect)