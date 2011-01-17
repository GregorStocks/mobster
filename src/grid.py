import pygame
from sprites import load_png

class Grid:
    def __init__(self, background_filename, cols, rows):
        '''Creates a grid, with size set by the background's size.'''
        picture, rect = load_png(background_filename)
        self.guys = []
        self.col_width = rect.width
        self.row_height = rect.height
        self.cols = cols
        self.rows = rows

        self.background = pygame.Surface((self.col_width * cols,
                                          self.row_height * rows))

        for x in xrange(self.cols):
            for y in xrange(self.rows):
                rect.topleft = (x*rect.width, y*rect.height)
                self.background.blit(picture, rect)

    def draw(self, screen):
        screen.blit(self.background, (0,0))
        for guy in self.guys:
            guy.draw(screen, (guy.x * self.col_width, guy.y * self.row_height))

    def add(self, guy):
        self.guys.append(guy)

    def remove(self, guy):
        self.guys.remove(guy)

