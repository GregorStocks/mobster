import pygame
from sprites import load_png

class Grid(object):
    def __init__(self, background_filename, cols, rows):
        '''Creates a grid, with size set by the background's size.'''
        picture, rect = load_png(background_filename)
        self.entities = {}
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
        for e, (x, y) in self.entities.items():
            e.draw(screen, (x * self.col_width, y * self.row_height))

    def add(self, e, pos):
        self.entities[e] = pos

    def remove(self, e):
        del self.entities[e]

    def move(self, e, delta):
        x, y = self.entities[e]
        dx, dy = delta
        x += dx
        y += dy
        if x >= self.cols or x < 0 or y >= self.rows or y < 0:
            return False
        self.entities[e] = (x, y)
        return True

    def collisions(self, entity):
        '''returns everything else in the grid with the same (x, y) as entity'''
        for e in self.at(self.entities[entity]):
            if e != entity:
                yield e

    def at(self, pos):
        '''returns all entities at (x, y)'''
        (x, y) = pos
        for e, (ex, ey) in self.entities.items():
            if x == ex and y == ey:
                yield e


