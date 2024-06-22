import sys
import pygame
from pygame.locals import *
from pages.main_page import main_page

if __name__=="__main__":
    pygame.init()
    pygame.display.set_caption("Fruit Cutting Game")
    
    screen = pygame.display.set_mode((700, 700))
    clock = pygame.time.Clock()

    main_page(screen, clock) # Call main page
