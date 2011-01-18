import pygame
from sprites import load_png
from pygame.font import Font
from pygame.color import Color

class UI:
    def __init__(self, grid):
        '''a UI right below the grid'''
        self.pos = (0, grid.rows * grid.row_height)
        self.font = Font(None, 12)
        self.background = pygame.Surface((grid.col_width * grid.cols, 50))
        self.background.fill(Color(255,255,255))

    def draw(self, screen, guy, enemy):
        screen.blit(self.background, self.pos)

        text = self.font.render('cool guy: %s%%' % guy.health, True, pygame.Color(0,0,0))
        screen.blit(text, self.pos)

        text = self.font.render('bad guy: %s%%' % enemy.health, True, pygame.Color(0,0,0))
        x, y = self.pos
        screen.blit(text, (x + 200, y))

