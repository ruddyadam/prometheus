#foodCursor.py

#a square white rect will track with the mouse

import pygame, sys
from pygame.locals import *

pygame.init()

screenRect = Rect(0,0,640,480)
screen = pygame.display.set_mode((screenRect.size),0,32)
color = (255,255,255)
radius = (10)
bg_image = 'aquarium.jpg'
background = pygame.image.load(bg_image).convert()
rectCentx = 2
rectCenty = 2
rectHei = 4
rectWid = 4


while True: #main game loop
    global x,y
    x,y = pygame.mouse.get_pos()
    food = Rect(x-rectCentx,y-rectCenty,rectHei,rectWid)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (True,False,False):
                #global foodPosList
                #foodPosTuple = pygame.mouse.get_pos()
                #for i in foodPosTuple:
                #    foodPosList.append(i)
                #need to store coordinates to be retrieved by
                #this draw.rect and stored so they can be deleted when food gets eaten.  bad idea.,
                xFood,yFood = pygame.mouse.get_pos()
                foodStamp = Rect(xFood-rectCentx,yFood-rectCenty,rectHei,rectWid)
                screen.lock()
                pygame.draw.rect(background, color, foodStamp, 0)
                screen.unlock()
                print xFood-rectCentx,'\'', yFood-rectCenty

            
    screen.blit(background, (0,0))
    
    screen.lock()
    #pygame.draw.circle(screen, color, pygame.mouse.get_pos(), radius)
    pygame.draw.rect(screen, color, food, 0)
    screen.unlock()

    #on mouseclick, stamp an image of the food
    #store food coordinates in an array, that will be the list we can delete from when they get eaten.
        

    pygame.display.update()
