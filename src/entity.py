#!/usr/bin/python

from sprites import load_png

class Entity(object):
    def __init__(self, filename):
        self.image, _ = load_png(filename)

    def draw(self, screen, pos):
        screen.blit(self.image, pos)
