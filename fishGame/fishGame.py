#fishGame.py

# place fish with right mouseclick
# place food with left mouseclick

# loop fish movement:
# update coordinates of fish / food
# draw fish
# draw fish eye
# draw food
# clear screen

"""
draw a shark sprite
    -shark points horizontally towards the closest food drop when dropped
        -shark location (updates with step)
        -all food locations (updates with step)
    -shark's mouth ('center' of sprite is mouth?) moves directly towards food when dropped
drop food sprite/animation on mouse click
    -will drop only on single mouse click, not on holding down mouse
    -will drop with each click
        -create food sprite instance with mouse click at mouse location  

FUTURE:
score
    -number on top shows how many food bits are on the screen.
    -another number shows how many food bits were eaten

"""



import pygame, sys
from pygame.locals import *

screenRect = Rect(0,0,640,480)  #sets the screen size
#screenSize = (640, 480)
#fpsClock = pygame.time.Clock()  #this is for syncing fps in the game.  currently unused
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
VIOLET = (208, 32, 144)
WHITE = (255, 255, 255)
bg_image = 'aquarium.jpg'
#shark = 'shark.png'
#food = 'dsham.png'
foodPos = [] # list of tuples of x,y coordinates of "food"
fishPos = [] # list of tuples of x,y coordinates of
#Nx,Ny = 0,0 # this is the nose coordinate of the fish, which will draw the rest of the body

#dFood = 
#moveList = [] # 3 item tuple: iterator, x pos, y pos
#fishIter = 0 # fish iterator: first fish = 1, second fish = 2, third fish = 3


def main():  #the main function
    pygame.init()  #this initializes pygame

    global background
    global screen
    screen = pygame.display.set_mode((screenRect.size),0,32) # this creates the screen
    pygame.display.set_caption('Ultimate Fish Game:             Right Click to place FISH  |  Left Click to place FOOD') # the title

    
    background = pygame.image.load(bg_image).convert() #this prepares the jpg image
    #mouse_cursor = pygame.image.load(food).convert_alpha() #this prepares the png image - 'alpha' for transparency
    #how about mouse_cursor = the food rect??  forget about image.load()
    #pygame.mouse.set_visible(False) #this hides the mouse pointer
    
    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (False, False, True): # if right click
                    #drawFish() #draws a persistent fish on right click
                    x, y = pygame.mouse.get_pos()
                    fishPos.append([x, y])
                    #fishPos.append(pygame.mouse.get_pos()) # creates a list of immutable tuples
                    print "fishPos = ", fishPos

                if pygame.mouse.get_pressed() == (True,False,False): # if left click
                    x, y = pygame.mouse.get_pos()
                    foodPos.append([x, y])
                    #foodPos.append(pygame.mouse.get_pos()) # creates a list of immutable tuples
                    print "foodPos = ", foodPos

        #screen.fill((0,0,0)) # clears screen/ fills the screen with black
        screen.blit(background, (0,0))      #this keeps redrawing the background
        drawFish() # draw fish based on right click
        fishPos = drawFish() # recreates fishPos with updated positions
        drawFood() # draw food based on left click
        moveFish() # moves fish 10 pixels closer to the the food, up to 10 pixels away -- COMBINE WITH eatFood() TO MAKE moveOrEat()
        # if Nx[n]-xFood[n] > 10 (move distance) pixels, and Ny[n]-yFood[n] != 0, moveFish() # moves all fish along
        # ... moveFish() iterates the first value of foodPos over fishPos, so each fish moves towards the same food.
        # if Nx[n]-xFood[n] < 10 (move distance) pixels, and Ny[n]-yFood[n] == 0, eatFood() # puts a fish on food location
        # possible bug if fish tie.  make it so closest fish (in pixels) wins
        # ... eatFood() iterates


        # screen.blit(mouse_cursor,(x,y))     #redraws the mouse cursor image at x,y (cursor position)
        
        pygame.display.update()  #not sure what this does

"""
def fishDist():
    # updates the moveList so fish can "move"

    #get the distance from fish nose to food, move 10 pixels along it.
    #create a line, plot nose coordinates along it.
    #calculate noseX and noseY based on a closer distance.
    #iterate over moveList.

    #currMoveList =
    for n in moveList:
        dist = int(math.hypot(n[0]-x, n[1]-y))
        closer =
        moveList = ["get closer along distance" for n in moveList]
"""

"""
def setFishPos(): # updates the moveList
    # if moveList is empty, create the first entry; fishIter may not be necessary
    moveList.append(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
"""

        #if n[0] == len(moveList): # adding to the list

def drawFish(): # draw every fish, using fishPos locations

        #global fishIter
        #global moveList
        #fishIter += 1



    for n in fishPos: # n[0] = x, n[1] = y coordinates

        relClicks = [(n[0]-90, n[1]+9), (n[0]-121, n[1]+20), (n[0]-120, n[1]-21), (n[0]-92, n[1]-3), (n[0]-39, n[1]-29), (n[0], n[1]), (n[0]-37, n[1]+24)]
        relCircleCen = (n[0]-33, n[1]-10)
        relCircleRad = 7



        screen.lock()
        pygame.draw.polygon(screen,BLUE,relClicks,0) # draw fish body
        pygame.draw.circle(screen,YELLOW,relCircleCen,relCircleRad,0) # draw fish eye

        screen.unlock()

def drawFood(): # draw every food, suing foodPos locations

    for n in foodPos:

        foodStamp = Rect(n[0],n[1],5,5)
        screen.lock()
        pygame.draw.rect(screen, WHITE, foodStamp, 0)
        screen.unlock()
        #print str(n[0]) + ',' + str(n[1])

def moveFishes(foodPos, fishPos):
    """
    Moves each fish towards the food.

    @param foodPos
    a list of 2-tuples which represent x, y coordinates of the food

    @param fishPos
    a list of 2-tuples which represent x,y coordinates of the fish

    @return
    returns a new list to be set to fishPos
    """

    for position in fishPos:




    if foodPos != []: # do not move fish unless there is food
        for tup in fishPos: # for each fish
            if abs(tup[1] - foodPos[0[1]]) > 10 and abs(tup[0] - foodPos[0[0]]) > 10: # if fish is above or below food by more than 10
                for coor in tup:
                    if coor > foodPos[0[coor]]: # if fishPos x or y is greater than foodPos x or y
                        fishPos.replace(tup[coor], tup[coor] - 10) # moves fish up or right by 10 pixels
                    else: # coor < foodPos[0[coor]] # if fishPos x or y is less than foodPos x or y
                        fishPos.replace(tup[coor], tup[coor] + 10) # moves fish down or left by 10 pixels


## todo:    stamp a ham on mouseclick
##          draw a shark on the page (and make it move towards food) 
##              -distance between "nose" point and center of food
##              -move a little each step in the loop
##              -

if __name__ == '__main__': #this allows import of this without automatic code execution
    main()  


#class sharkSprite(pygame.sprite.Sprite):
    
#class foodSprite(pygame.sprite.Sprite):





"""
        if event.type == KEYDOWN:
            if event.key = K_RIGHT:
                flip_x = True
            elif event.key = K_LEFT:
                flip_x = False


        new_image = pygame.transform.flip(image, flip_x, False)
"""
    
