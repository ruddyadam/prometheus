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

SCREENRECT = Rect(0,0,640,480)
#screenSize = (640, 480)
fpsClock = pygame.time.Clock()
BLUE = (0, 0, 255)
bg_image = 'aquarium.jpg'
shark = 'shark.png'
food = 'dsham.png'


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREENRECT.size),0,32)
    pygame.display.set_caption('Ultimate Fish Game')
    
    background = pygame.image.load(bg_image).convert()
    mouse_c = pygame.image.load(shark).convert_alpha()
    
    #bg = screen.fill(BLUE)
    
    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background, (0,0))   

        x,y = pygame.mouse.get_pos()
        x -= mouse_c.get_width()/2
        y -= mouse_c.get_height()/2

        screen.blit(mouse_c,(x,y))

        pygame.display.update()



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
        
    
