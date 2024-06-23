import sys
import pygame
import random
from pygame.locals import *
from element.game.fruit import Fruit
from element.game.trail import Trail
from element.game.splash import Splash
from element.game.ui import Scorer, Counter
from pages.game_end_page import game_end_page
from data.fruit import fruits_data

def is_safe(pos):
    return 0<=pos[0] and pos[0]<=700 and 0<=pos[1] and pos[1]<=700

def game_page(screen, clock):
    fruits = []
    splashs = []

    trail = Trail((245, 245, 245), 6)

    life = Counter("LIFE", 32, [100, 50], (0, 0, 255), 3, -1)
    score = Scorer("SCORE", 32, [350, 50], (0, 0, 255))

    running = True
    while running:
        screen.fill((255, 255, 255))

        mx, my = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()[0]

        if press:
            trail.add((mx, my))
        trail.update()

        if len(fruits)<1:
            fruits.append(Fruit(random.choice(list(fruits_data.keys())), [random.randint(100, 600), 700], (80, 80)))
            fruits_data[fruits[-1].name]["visible"] = True
        for fruit in fruits:
            if is_safe(fruit.pos):
                if press and fruit.cuttable and fruit.rect.collidepoint((mx, my)):
                    fruit.cuttable = False
                    fruit.set_image(3)
                    score.update(fruits_data[fruit.name]["score"])
                    splashs.append(Splash(fruit.pos, fruit.size, fruit.name))
                fruit.update()
            else:
                if fruit.cuttable:
                    life.update()
                fruits.remove(fruit)

        for splash in splashs:
            splash.update()
            if splash.time<=0:
                splashs.remove(splash)

        for splash in splashs:
            splash.draw(screen)

        for fruit in fruits:
            fruit.draw(screen)
            
        trail.draw(screen)
        life.draw(screen)
        score.draw(screen)

        if life.get_value()<=0:
            game_end_page(screen, clock, score.get_value())
            running = False

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    running = False
        
        pygame.display.update()
        clock.tick(60)