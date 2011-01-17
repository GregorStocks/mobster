#!/usr/bin/python

from weapon import Weapon
from entity import Entity
from pygame.font import Font
import pygame

class Guy (Entity):
    def __init__(self, filename, x, y):
        Entity.__init__(self, filename, x, y)
        self.health = 100
        self.weapon = Weapon(5)
        self.font = Font(None, 12)

    def draw(self, screen, pos):
        Entity.draw(self, screen, pos)
        text = self.font.render('%s%%' % self.health, True, pygame.Color(0,0,0))
        screen.blit(text, pos)
