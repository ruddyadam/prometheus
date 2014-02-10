# fishEat.py
#this program will take resources from drawFish.py and drawFood.py and make them work together to make a fish eat food.

#fish and food need to be blittable objects.


import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
bg_image = 'aquarium.jpg'
background = pygame.image.load(bg_image).convert()

BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
foodPosTuple = []

def drawFish(): # draws a polygon fish relative to the cursor position, cursor pos is its "nose".
    #this requires 'screen' var to be set, e.g.  screen = pygame.display.set_mode((640,480),0,32)


    #Nx = 161
    #Ny = 77
    #dNose = (Nx, Ny)
    Nx,Ny = pygame.mouse.get_pos()
    # defClicks = [(Nx-n[0], Ny-n[1]) for n in dClicks]
    defClicks = [
        (Nx-90, Ny+9), (Nx-121, Ny+20), (Nx-120, Ny-21),
        (Nx-92, Ny-3), (Nx-39, Ny-29), (Nx, Ny),
        (Nx-37, Ny+24)]
    defCircleCen = (Nx-33, Ny-10)
    defCircleRad = 7

    bodyColor = BLUE
    eyeColor = YELLOW

    screen.lock()
    pygame.draw.polygon(screen,bodyColor,defClicks,0)
    screen.unlock()
    screen.lock()
    pygame.draw.circle(screen,eyeColor,defCircleCen,defCircleRad,0)
    screen.unlock()

def drawFood():

    rectOffx = 1
    rectOffy = 1
    rectHei = 4
    rectWid = 4


    if pygame.mouse.get_pressed() == (True,False,False):

        xFood,yFood = pygame.mouse.get_pos()

        #global foodPosTuple #this is to be used to direct fish and to delete food when eaten.  and a surprise.
        foodPosTuple.append((xFood-rectOffx, yFood-rectOffy)) #this creates a list of 'food' center pixel positions (x,y)

        print "foodPosTuple = ", foodPosTuple


        foodStamp = Rect(xFood-rectOffx,yFood-rectOffy,rectHei,rectWid)
        currFoodx = xFood-rectOffx
        currFoody = yFood-rectOffy
        food = pygame.draw.rect(background, WHITE, foodStamp, 0)
        screen.lock()
        pygame.draw.rect(background, WHITE, foodStamp, 0)
        screen.unlock()

        print "last coordinate: ", str(xFood-rectOffx) +','+ str(yFood-rectOffy)
        print type(food)
        return food


#def moveFish():



def main():

    screen.blit(background, (0,0)) # background will not refresh, is outside of the loop

    while True: #main game loop

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()



            if event.type == MOUSEBUTTONDOWN:
                drawFood()
                #screen.blit(drawFood(), (foodPosTuple))

            if event.type == KEYDOWN:
                if event.key == K_TAB:
                    drawFish()


        pygame.display.update()

if __name__ == '__main__':
    main()