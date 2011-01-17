#!/usr/bin/python

import sys, pygame
from pygame.locals import *
from sprites import load_png

def background(screen, picture):
    rect = picture.get_rect()
    rows = screen.get_height()//rect.height + 1
    cols = screen.get_width()//rect.width + 1
    for x in range(cols):
        for y in range(rows):
            rect.topleft = (x*rect.width, y*rect.height)
            screen.blit(picture, rect)

class Guy:
    def __init__(self, filename):
        self.x = 3
        self.y = 1
        self.image, self.rect = load_png(filename)

    def draw(self):
        self.rect.topleft = (self.x * self.rect.width,
                             self.y * self.rect.height)
        screen.blit(self.image, self.rect)

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    guy = Guy('dude')
    grass, _ = load_png('grass')
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
                    

        background(screen, grass)
        guy.draw()
        pygame.display.flip()
