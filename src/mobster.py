#!/usr/bin/python

import sys, pygame
from pygame.locals import *
from sprites import load_png

class Grid:
    def __init__(self, screen, background_filename):
        '''Creates a grid, with size set by the background's size.'''
        picture, rect = load_png(background_filename)
        self.screen = screen
        self.guys = []
        self.col_width = rect.width
        self.row_height = rect.height

        width = screen.get_width()
        height = screen.get_height()
        self.background = pygame.Surface((width, height))

        cols = width//rect.width + 1
        rows = height//rect.height + 1

        for x in range(cols):
            for y in range(rows):
                rect.topleft = (x*rect.width, y*rect.height)
                self.background.blit(picture, rect)

    def draw(self):
        self.screen.blit(self.background, (0,0))
        for guy in self.guys:
            self.screen.blit(guy.image, (guy.x * self.col_width,
                                         guy.y * self.row_height))

    def add(self, guy):
        self.guys.append(guy)

class Guy:
    def __init__(self, filename):
        self.x = 3
        self.y = 1
        self.image, _ = load_png(filename)

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    grid = Grid(screen, 'grass')
    guy = Guy('dude')
    grid.add(guy)
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
                    
        grid.draw()
        pygame.display.flip()
