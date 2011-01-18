#!/usr/bin/python

import sys, pygame
from pygame.locals import *
from grid import Grid
from guy import Guy
from entity import Entity
from ui import UI
from action import *

def update_screen(grid, ui, screen, guys, enemies):
    grid.draw(screen)
    ui.draw(screen, guys, enemies)
    pygame.display.flip()

def handle_key(grid, ui, screen, key, guys, curguy):
    guy = guys[curguy]
    action = None
    if key == K_UP or key == K_DOWN or key == K_LEFT or key == K_RIGHT:
        action = Move(guy, key)
    elif event.key == K_RETURN:
        action = Shoot(grid.entities[guy], guy.weapon.range)
    if action != None:
        if not action.execute(grid, screen, ui, guys, enemies):
            return curguy
    return (curguy + 1) % len(guys)

def move_enemies(grid, ui, screen, guys, enemies):
    for enemy in enemies:
        action = Shoot(grid.entities[enemy], enemy.weapon.range)
        action.execute(grid, screen, ui, guys, enemies)

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((800, 600))


    grid = Grid('grass', 10, 6)
    ui = UI(grid)

    guys = []
    enemies = []
    for x in xrange(2):
        for y in xrange(4):
            guy = Guy('dude')
            grid.add(guy, (x*2 + 1 + y % 2, y))
            guys.append(guy)

            enemy = Guy('dude')
            enemy.image = pygame.transform.flip(enemy.image, True, False)
            grid.add(enemy, (x*2 + 6 + y % 2, y))
            enemies.append(enemy)

    curguy = 0
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                prevguy = curguy
                curguy = handle_key(grid, ui, screen, event.key, guys, curguy)
                if prevguy > curguy: # looped around
                    move_enemies(grid, ui, screen, guys, enemies)
        update_screen(grid, ui, screen, guys, enemies)
