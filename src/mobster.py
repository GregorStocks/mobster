#!/usr/bin/python

import sys, pygame

def background(screen, picture):
    rect = picture.get_rect()
    rows = 480//rect.height + 1
    cols = 640//rect.width + 1
    for x in range(cols):
        for y in range(rows):
            rect.topleft = (x*rect.width, y*rect.height)
            screen.blit(picture, rect)



if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    guy = pygame.image.load('data/dude.png').convert()
    grass = pygame.image.load('data/grass.png').convert()
    pos = guy.get_rect()
    pos = pos.move((200, 0))
    pos = pos.move((0, 50))
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        background(screen, grass)
        screen.blit(guy, pos)
        pygame.display.flip()
