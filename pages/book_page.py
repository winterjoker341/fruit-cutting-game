import pygame
from pygame.locals import *

def book_page(screen, clock):
    running = True
    while running:
        screen.fill((0, 0, 255))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(60)