#drawFish.py
"""
this quick and dirty fish image coordinate maker took me 5+ hours
Usage:
-Left click: 3 or more times to create a blue polygon
-Right click: click and drag to create a circle with radius of drag distance
-Enter: returns the coordinates of polygon, circle, and circle radius
-Tab: draw a default fish
-Escape: clear the screen

update: now Tab draws a fish at cursor position, with all body coordinates relative to it.



"""
import pygame, sys
from pygame.locals import *
#from Tkinter import Tk
import math

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption('3+ L-clicks: polygon | Drag R-click: eye | ESC: clear | Enter: coords | Tab: draw fish at cursor')

FISH_BLUE = (0, 0, 255)
FISH_YELLOW = (255, 255, 0)

# make dClicks coordinates relative to cursor position, and K_TAB or a click stamps the image at the cursor coordinates,
# keeping every "stamp" an entity that will react to the presence of "food".
#    -collision polygon collision detection? (possibly necessitating code refactor)


dClicks = [(71, 86), (40, 97), (41, 56), (69, 74), (122, 48), (161, 77), (124, 101)]
dCircleCen = (128, 67)
dCircleRad = 7

x1,x2,x3,y1,y2,y3 = 0,0,0,0,0,0

def relDrawFish(): # draws a polygon fish relative to the cursor position, cursor pos is its "nose".
    #this requires 'screen' var to be set, e.g.  screen = pygame.display.set_mode((640,480),0,32)


    #Nx = 161
    #Ny = 77
    #dNose = (Nx, Ny)
    Nx,Ny = pygame.mouse.get_pos()
    # defClicks = [(Nx-n[0], Ny-n[1]) for n in dClicks]
    defClicks = [(Nx-90, Ny+9), (Nx-121, Ny+20), (Nx-120, Ny-21), (Nx-92, Ny-3), (Nx-39, Ny-29), (Nx, Ny), (Nx-37, Ny+24)]
    defCircleCen = (Nx-33, Ny-10)
    defCircleRad = 7

    bodyColor = FISH_BLUE
    eyeColor = FISH_YELLOW

    screen.lock()
    pygame.draw.polygon(screen,bodyColor,defClicks,0)
    screen.unlock()
    screen.lock()
    pygame.draw.circle(screen,eyeColor,defCircleCen,dCircleRad,0)
    screen.unlock()


def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            clicks = []
            circleCenter = (0,0)
            circleRad = 0

            if event.type == pygame.MOUSEBUTTONDOWN: # ensures no dragging
                if pygame.mouse.get_pressed() == (True, False, False): # if left click
                    clicks.append(pygame.mouse.get_pos()) # append (x,y) points to 'clicks' variable
                if pygame.mouse.get_pressed() == (False, False, True): # if right click
                    circleCenter = x1,y1 = (pygame.mouse.get_pos())

            if pygame.mouse.get_pressed() == (False, False, True): # right click
                x2, y2 = pygame.mouse.get_pos()
                circleRad = int(math.hypot(abs(x1-x2), abs(y1-y2)))
                # print circleRad
                          
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    clicks = [] # erases polygon
                    circleRad = 0 # erases circle(s)
                    screen.fill((0,0,0)) # fills the screen with black
            
                if event.key == K_RETURN:
                    print "polygon coordinates: ", clicks  # prints to console/shell
                    print "circleCenter: ", circleCenter
                    print "circle radius: ", circleRad

                if event.key == K_TAB: # draws a small fish using dClick, dCircleCenter, dCircleRad
                    relDrawFish()

                """
                    #overwrites polygon coordinates to tuples.txt file, closes
                    f = open('tuples.txt', 'w')
                    f.write('a')
                    foo()
                    f.close()

                
                    with open('tuples.txt', 'w') as f: # 'a' to append
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
                    if clicks != [] or (circleRad != 0):
                        clicks = [] # erases polygon
                        circleRad = 0 #erases circle(s)
                        screen.fill((0,0,0)) #fills the screen with black
                        screen.lock()
                        pygame.draw.polygon(screen,BLUE,dClicks,0)
                        screen.unlock()
                        screen.lock()
                        pygame.draw.circle(screen,YELLOW,dCircleCenter,dcircleRad,0)
                        screen.unlock()
                """
                """
                if event.key == K_TAB: # draws a small fish using dClick, dCircleCenter, dCircleRad
                    screen.lock()
                    pygame.draw.polygon(screen,FISH_BLUE,dClicks,0)
                    screen.unlock()
                    screen.lock()
                    pygame.draw.circle(screen,FISH_YELLOW,dCircleCen,dCircleRad,0)
                    screen.unlock()
                """


        
        if len(clicks) > 2: # polygon must contain 3 or more points
            screen.lock()
            pygame.draw.polygon(screen,FISH_BLUE,clicks,0)
            screen.unlock()

        if circleRad > 0:
            screen.lock()
            pygame.draw.circle(screen,FISH_YELLOW,circleCenter,circleRad,0)
            screen.unlock()

        pygame.display.update()

# change the code so all the points on the polygon are in reference to a single point, the 'nose'.
# this will make moving the fish more modular, as only the nose point and the food point will need to be calculated
# then as the nose moves, the rest of the fish does as well, form a different method, bodyCoords().
#

"""
def moveFish(coords, circleCen):
    x,y = pygame.mouse.get_pos()
    movingpoints = []
    for n in coords:
        n[0]
"""


if __name__ == '__main__':
    main()