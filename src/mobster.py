#!/usr/bin/python

import sys, pygame

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    guy = pygame.image.load('data/dude.png').convert()
    pos = guy.get_rect()
    pos = pos.move((200, 0))
    pos = pos.move((0, 50))
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0,0,0))
        screen.blit(guy, pos)
        pygame.display.flip()
