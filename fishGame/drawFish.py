#drawFish.py
"""
this quick and dirty fish image coordinate maker took me 5+ hours
Usage:
-Left click: 3 or more times to create a blue polygon
-Right click: click and drag to create a circle with radius of drag distance
-Enter: returns the coordinates of polygon, circle, and circle radius
-Tab: draw a default fish
-Escape: clear the screen

"""
import pygame, sys
from pygame.locals import *
#from Tkinter import Tk
import math

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption('3+ L-clicks: polygon | Drag R-click: eye | ESC: clear | Enter: coords | Tab: a fish')
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

clicks = []
circleCenter = (0,0)
circleRad = 0
 
defClicks = [(71, 86), (40, 97), (41, 56), (69, 74), (122, 48), (161, 77), (124, 101)]
defCircleCenter = (128, 67)
defCircleRad = 7

x1,x2,x3,y1,y2,y3 = 0,0,0,0,0,0



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN: #ensures no dragging
            if pygame.mouse.get_pressed() == (True, False, False): #if left click
                clicks.append(pygame.mouse.get_pos()) #append (x,y) points to clicks
            if pygame.mouse.get_pressed() == (False, False, True): #if right click
                circleCenter = x1,y1 = (pygame.mouse.get_pos())

        if pygame.mouse.get_pressed() == (False, False, True):
            circleRad = 0
            x2, y2 = pygame.mouse.get_pos()
            circleRad = int(math.hypot(abs(x1-x2), abs(y1-y2)))
            #print circleRad
                          
                
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                clicks = [] #erases polygon
                circleRad = 0 #erases circle(s)
                screen.fill((0,0,0)) #fills the screen with black
            
            if event.key == K_RETURN:
                print "polygon coordinates: ", clicks  #prints to console/shell
                print "circleCenter: ", circleCenter
                print "circle radius: ", circleRad
                """
                #overwrites polygon coordinates to tuples.txt file, closes
                with open('tuples.txt', 'w') as f: #'a' to append
                    f.write(str(clicks).strip('[]'))

                #copies polygon coordinates to clipboard
                c = Tk()
                c.withdraw()
                c.clipboard_clear()
                c.clipboard_append(str(clicks).strip('[]'))
                c.destroy()
                """
            """
            if event.key == K_SPACE:
                if (clicks not []) and (circleRad not == 0):
                    clicks = [] #erases polygon
                    circleRad = 0 #erases circle(s)
                    screen.fill((0,0,0)) #fills the screen with black
                    screen.lock()
                    pygame.draw.polygon(screen,BLUE,defClicks,0)
                    screen.unlock()
                    screen.lock()
                    pygame.draw.circle(screen,YELLOW,defCircleCenter,circleRad,0)
                    screen.unlock()
            """
            if event.key == K_TAB:
                screen.lock()
                pygame.draw.polygon(screen,BLUE,defClicks,0)
                screen.unlock()
                screen.lock()
                pygame.draw.circle(screen,YELLOW,defCircleCenter,defCircleRad,0)
                screen.unlock()
                


        
    if len(clicks) > 2: #polygon must contain 3 or more points
        screen.lock()
        pygame.draw.polygon(screen,BLUE,clicks,0)
        screen.unlock()

    if circleRad > 0:
        screen.lock()
        pygame.draw.circle(screen,YELLOW,circleCenter,circleRad,0)
        screen.unlock()
    
    pygame.display.update() 
