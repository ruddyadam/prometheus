#fishGame.py
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

screenSize = Rect(0,0,640,480)  #sets the screen size
#screenSize = (640, 480)
fpsClock = pygame.time.Clock()  #this is for syncing fps in the game.  currently unused
BLUE = (0, 0, 255)
bg_image = 'aquarium.jpg'
shark = 'shark.png'
food = 'dsham.png'


def main():  #the main?
    pygame.init()  #this initializes mygame

    screen = pygame.display.set_mode((screenSize.size),0,32)  #this creates the screen
    pygame.display.set_caption('Ultimate Fish Game')#the title
    
    background = pygame.image.load(bg_image).convert() #this prepares the jpg image
    mouse_cursor = pygame.image.load(food).convert_alpha() #this prepares the png image - 'alpha' for transparency
    pygame.mouse.set_visible(False)         #this hides the mouse pointer
    
    #bg = screen.fill(BLUE)
    
    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background, (0,0))      #this keeps redrawing the background, so no trails on mouse_cursor image

        x,y = pygame.mouse.get_pos()        #gets the mouse position
        x -= mouse_cursor.get_width()/2     #these get the center of the mouse cursor image
        y -= mouse_cursor.get_height()/2    #these get the center of the mouse cursor image

        screen.blit(mouse_cursor,(x,y))     #not sure what this does

        pygame.display.update()  #not sure what this does

## todo:    stamp a ham on mouseclick
##          draw a shark on the page (and make it move towards food) 
##          
##


main()  #starts the main() def


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
        
    
