#!/usr/bin/python

from weapon import Weapon
from entity import Entity
import pygame

class Guy (Entity):
    def __init__(self, filename):
        Entity.__init__(self, filename)
        self.health = 100
        self.weapon = Weapon(5)
