#!/usr/bin/python

import sys, pygame
from pygame.locals import *
from sprites import load_png

class Grid:
    def __init__(self, background_filename, cols, rows):
        '''Creates a grid, with size set by the background's size.'''
        picture, rect = load_png(background_filename)
        self.screen = screen
        self.guys = []
        self.col_width = rect.width
        self.row_height = rect.height
        self.cols = cols
        self.rows = rows

        self.background = pygame.Surface((self.col_width * cols,
                                          self.row_height * rows))

        for x in range(self.cols):
            for y in range(self.rows):
                rect.topleft = (x*rect.width, y*rect.height)
                self.background.blit(picture, rect)

    def draw(self, screen):
        screen.blit(self.background, (0,0))
        for guy in self.guys:
            screen.blit(guy.image, (guy.x * self.col_width,
                                    guy.y * self.row_height))

    def add(self, guy):
        self.guys.append(guy)

class Guy:
    def __init__(self, filename, x, y):
        self.x = x
        self.y = y
        self.image, _ = load_png(filename)

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((640, 480))

    guy = Guy('dude', 2, 4)
    enemy = Guy('dude', 8, 4)
    enemy.image = pygame.transform.flip(enemy.image, True, False)

    grid = Grid('grass', 10, 6)
    grid.add(guy)
    grid.add(enemy)
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    guy.y -= 1
                elif event.key == K_DOWN:
                    guy.y += 1
                elif event.key == K_LEFT:
                    guy.x -= 1
                elif event.key == K_RIGHT:
                    guy.x += 1
                    
        grid.draw(screen)
        pygame.display.flip()
