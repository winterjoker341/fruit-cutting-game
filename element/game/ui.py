import pygame
from element.base.text import Text

class Counter:
    def __init__(self, name, size, pos, color, value, weight):
        self.name = name
        self._value = value
        self._weight = weight
        self.text = Text(f"{self.name} : {self._value}", pos, size, color)

    def update(self):
        self._value += self._weight
        self.text.update(f"{self.name} : {self._value}")

    def draw(self, screen):
        self.text.draw(screen)

    def get_value(self):
        return self._value

class Scorer:
    def __init__(self, name, size, pos, color):
        self.name = name
        self._value = 0
        self.text = Text(f"{self.name} : {self._value}", pos, size, color)

    def update(self, value):
        self._value += value
        self.text.update(f"{self.name} : {self._value}")

    def draw(self, screen):
        self.text.draw(screen)

    def get_value(self):
        return self._value
