import sys
import pygame
from pygame.locals import *
from element.book.book import Book
from element.base.text import Text
from data.fruit import fruits_data

def book_page(screen, clock):
    title = Text("Book", (350, 100), 42, (0, 0, 255))

    book_list = []
    for i in range(3):
        for j in range(4):
            if i*4+j<len(fruits_data):
                book_color = (0, 0, 255)
            else:
                book_color = (0, 255, 0)
            book_list.append(Book([j*150+125, i*150+250], [100, 100], book_color))

    for i, fruit in enumerate(fruits_data):
        if fruits_data[fruit]["visible"]==True:
            book_list[i].set_image(fruit)

    running = True
    while running:
        screen.fill((255, 255, 255))

        title.draw(screen)
        for book in book_list:
            book.draw(screen)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(60)