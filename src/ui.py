import pygame
from sprites import load_png
from pygame.font import Font
from pygame.color import Color

class UI(object):
    def __init__(self, grid):
        '''a UI right below the grid'''
        self.pos = (0, grid.rows * grid.row_height)
        self.font = Font(None, 12)
        self.background = pygame.Surface((grid.col_width * grid.cols, 100))
        self.background.fill(Color(255,255,255))

    def draw(self, screen, guys, enemies):
        screen.blit(self.background, self.pos)

        x, y = self.pos
        for (x, desc, list) in [(x, 'cool guy', guys), (x + 200, 'enemy', enemies)]:
            guynum = 0
            for guy in list:
                str = '%s #%s: %s%%' % (desc, guynum + 1, guy.health)
                text = self.font.render(str, True, pygame.Color(0,0,0))
                screen.blit(text, (x, y + guynum * 13))
                guynum += 1

