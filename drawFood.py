#foodCursor.py

#a square white rect will track with the mouse

import pygame, sys
from pygame.locals import *

pygame.init()

screenSize = Rect(0,0,640,480)
screen = pygame.display.set_mode((screenSize.size),0,32)
color = (255,255,255)
radius = (10)
#bg_image = 'aquarium.jpg'
#background = pygame.image.load(bg_image).convert()


while True: #main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    
    screen.lock()
    pygame.draw.circle(screen, color, pygame.mouse.get_pos(), radius)
    screen.unlock()

    screen.blit(screen, (0,0))


    pygame.display.update()
