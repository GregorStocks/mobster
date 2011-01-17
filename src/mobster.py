#!/usr/bin/python

import sys, pygame
from pygame.locals import *
from grid import Grid
from guy import Guy

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((640, 480))

    guy = Guy('dude', 2, 4)
    enemy = Guy('dude', 8, 4)
    enemy.image = pygame.transform.flip(enemy.image, True, False)

    grid = Grid('grass', 10, 6)
    grid.add(guy)
    grid.add(enemy)
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
                elif event.key == K_RETURN:
                    # shoot a bullet!
                    # this is a bad way to do it
                    bullet = Guy('bullet', guy.x + 1, guy.y)
                    grid.add(bullet)
                    for x in xrange(guy.weapon.range):
                        grid.draw(screen)
                        pygame.display.flip()
                        bullet.x += 1
                        pygame.time.wait(100)
                    grid.remove(bullet)
                    
        grid.draw(screen)
        pygame.display.flip()
