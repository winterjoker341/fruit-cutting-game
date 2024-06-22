import sys
import pygame
from pygame.locals import *
from element.base.text import Text

def game_end_page(screen, clock, score):
    your_score = Text(f"Your score is {score}", (350, 300), 40, (0, 0, 255))
    announse = Text("Press ESC to return to the start screen", (350, 400), 24, (0, 0, 255))

    running = True
    while running:
        screen.fill((255, 255, 255))

        announse.draw(screen)
        your_score.draw(screen)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(60)