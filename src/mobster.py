#!/usr/bin/python

import sys, pygame
from pygame.locals import *
from grid import Grid
from guy import Guy
from entity import Entity
from ui import UI

def update_screen(grid, ui, screen):
    grid.draw(screen)
    ui.draw(screen, guy, enemy)
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((640, 480))

    guy = Guy('dude')
    enemy = Guy('dude')
    enemy.image = pygame.transform.flip(enemy.image, True, False)

    grid = Grid('grass', 10, 6)
    ui = UI(grid)
    grid.add(guy, (4, 5))
    grid.add(enemy, (7, 5))
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    grid.move(guy, (0, -1))
                elif event.key == K_DOWN:
                    grid.move(guy, (0, 1))
                elif event.key == K_LEFT:
                    grid.move(guy, (-1, 0))
                elif event.key == K_RIGHT:
                    grid.move(guy, (1, 0))
                elif event.key == K_RETURN:
                    # shoot a bullet!
                    # this is a bad way to do it
                    bullet = Entity('bullet')
                    grid.add(bullet, (grid.entities[guy]))
                    for x in xrange(guy.weapon.range):
                        grid.move(bullet, (1, 0))
                        update_screen(grid, ui, screen)
                        done = False
                        for e in grid.collisions(bullet):
                            if e == enemy:
                                enemy.health -= 10
                                done = True
                        if done:
                            break
                        pygame.time.wait(100)
                    grid.remove(bullet)
                    
        update_screen(grid, ui, screen)
