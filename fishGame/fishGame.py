#fishGame.py

import pygame, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Ultimate Fish Game')

while True: #main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
    
