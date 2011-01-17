#!/usr/bin/python

import pygame, os

def load_png(name):
    '''load_png("poop") loads data/poop.png and returns (image, rect)'''
    path = os.path.join('data', name + '.png')
    img = pygame.image.load(path).convert_alpha()
    return img, img.get_rect()
