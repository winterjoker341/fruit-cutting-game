import sys
import pygame
from pygame.locals import *
from pages.game_page import game_page
from pages.rank_page import rank_page
from pages.book_page import book_page

def main_page(screen, clock):
    click = False

    while True:
        screen.fill((255, 255, 255))

        mx, my = pygame.mouse.get_pos()

        game_btn = pygame.Rect(50, 500, 100, 50)
        rank_btn = pygame.Rect(300, 500, 100, 50)
        book_btn = pygame.Rect(550, 500, 100, 50)

        if game_btn.collidepoint((mx, my)) and click:
            game_page(screen, clock)
        if rank_btn.collidepoint((mx, my)) and click:
            rank_page(screen, clock)
        if book_btn.collidepoint((mx, my)) and click:
            book_page(screen, clock)
    
        pygame.draw.rect(screen, (255, 0, 0), game_btn)
        pygame.draw.rect(screen, (0, 255, 0), rank_btn)
        pygame.draw.rect(screen, (0, 0, 255), book_btn)

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