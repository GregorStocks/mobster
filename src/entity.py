#!/usr/bin/python

from sprites import load_png

class Entity:
    def __init__(self, filename, x, y):
        self.x = x
        self.y = y
        self.image, _ = load_png(filename)

    def draw(self, screen, pos):
        screen.blit(self.image, pos)
