import sys
import pygame
from pygame.locals import *
from pages.game_page import game_page
from pages.rank_page import rank_page
from pages.book_page import book_page
from element.base.text import Text
from element.main.button import Button

def main_page(screen, clock):
    title = Text("Fruit Cutting Game", (350, 300), 50, (0, 0, 255))

    game_btn = Button([50, 500], [100, 50], (255, 0, 0))
    rank_btn = Button([300, 500], [100, 50], (0, 255, 0))
    book_btn = Button([550, 500], [100, 50], (0, 0, 255))

    click = False

    while True:
        screen.fill((255, 255, 255))

        mx, my = pygame.mouse.get_pos()

        if game_btn.isCollised((mx, my)) and click:
            game_page(screen, clock)
        if rank_btn.isCollised((mx, my)) and click:
            rank_page(screen, clock)
        if book_btn.isCollised((mx, my)) and click:
            book_page(screen, clock)
    
        title.draw(screen)
        game_btn.draw(screen)
        rank_btn.draw(screen)
        book_btn.draw(screen)

        click = False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    click = True
        
        pygame.display.update()
        clock.tick(60)