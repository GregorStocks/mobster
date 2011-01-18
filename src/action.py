#!/usr/bin/python
import mobster
from entity import Entity
from pygame.locals import *
import pygame

class Action(object):
    def execute(self, grid, screen, ui, guys, enemies):
        '''true if something happened, false otherwise'''
        pass

class Shoot(Action):
    def __init__(self, pos, range):
        self.pos = pos
        self.range = range

    def execute(self, grid, screen, ui, guys, enemies):
        # this is a bad way to do it
        bullet = Entity('bullet')
        grid.add(bullet, self.pos)
        for x in xrange(self.range):
            grid.move(bullet, (1, 0))
            mobster.update_screen(grid, ui, screen, guys, enemies)
            done = False
            for e in grid.collisions(bullet):
                for enemy in enemies:
                    if e == enemy:
                        enemy.health -= 10
                        done = True
            if done:
                break
            pygame.time.wait(100)
        grid.remove(bullet)
        return True

class Move(Action):
    def __init__(self, guy, key):
        if key == K_UP:
            self.move = ( 0, -1)
        elif key == K_DOWN:
            self.move = ( 0,  1)
        elif key == K_LEFT:
            self.move = (-1,  0)
        elif key == K_RIGHT:
            self.move = ( 1,  0)
        self.guy = guy

    def execute(self, grid, screen, ui, guys, enemies):
        collision = False
        x, y = grid.entities[self.guy]
        dx, dy = self.move
        for e in grid.at((x + dx, y + dy)):
            # if there's something there, abort
            collision = True
        if collision: return False
        grid.move(self.guy, self.move)
        return True
