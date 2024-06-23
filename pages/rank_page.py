import sys
import pygame
from pygame.locals import *
from element.rank.rank import Rank
from element.base.text import Text
from data.rank import rank_data

def rank_page(screen, clock):
    title = Text("Rank", (350, 100), 42, (0, 0, 255))

    rank_list = []
    for i, score in enumerate(rank_data):
        rank_list.append(Rank(i+1, score, [350, i*120+250], [500, 80], (0, 255, 0)))

    running = True
    while running:
        screen.fill((255, 255, 255))

        title.draw(screen)
        for rank in rank_list:
            rank.draw(screen)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(60)