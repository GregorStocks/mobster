#!/usr/bin/python

import sys, pygame
from pygame.locals import *
from grid import Grid
from guy import Guy
from entity import Entity
from ui import UI

def update_screen(grid, ui, screen, guys, enemies):
    grid.draw(screen)
    ui.draw(screen, guys, enemies)
    pygame.display.flip()

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
                guy = guys[curguy]
                move = None
                if event.key == K_UP:
                    move = (0, -1)
                elif event.key == K_DOWN:
                    move = (0, 1)
                elif event.key == K_LEFT:
                    move = (-1, 0)
                elif event.key == K_RIGHT:
                    move = (1, 0)
                elif event.key == K_RETURN:
                    # shoot a bullet!
                    # this is a bad way to do it
                    bullet = Entity('bullet')
                    grid.add(bullet, (grid.entities[guy]))
                    for x in xrange(guy.weapon.range):
                        grid.move(bullet, (1, 0))
                        update_screen(grid, ui, screen, guys, enemies)
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
                if move != None:
                    x, y = grid.entities[guy]
                    dx, dy = move
                    collision = False
                    for e in grid.at((x + dx, y + dy)):
                        # if there's something there, abort
                        collision = True
                    if collision: continue
                    grid.move(guy, move)
                curguy = (curguy + 1) % len(guys)
                    
        update_screen(grid, ui, screen, guys, enemies)
