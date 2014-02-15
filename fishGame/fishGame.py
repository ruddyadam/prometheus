#fishGame.py

import pygame, sys
from pygame.locals import *

screenRect = Rect(0,0,640,480)  #sets the screen size
#screenSize = (640, 480)

fps_clock = pygame.time.Clock()  #this is for syncing fps in the game.
fps = 200 # maximum frames per second (main loops per 1000 microseconds)
fish_move_distance = 1 # in pixels

BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
VIOLET = (208, 32, 144)
WHITE = (255, 255, 255)
bg_image = 'aquarium.jpg'

#todo: make the fish move less fast, but do not reduce FPS, or some clicks will not register.
#todo: set up a counter in the fish loop, that the fish will only move after each fish's position is re-updated 10 times.
#todo: this will make each fish 10x slower by design, without reducing the fps (amount of main loops per second)

def main(): #the main function
    pygame.init()  #this initializes pygame

    global background
    global screen
    #global food_positions and fish_positions are needed for the 'Escape' key to work.
    food_positions = [] # a list of tuples containing x,y coordinates of 'food'
    fish_positions = [] # a list of tuples containing x,y coordinates of the 'nose' of the fish
    screen = pygame.display.set_mode((screenRect.size),0,32) # this creates the screen
    pygame.display.set_caption('Ultimate Fish Game:             Right Click : FISH  |  Left Click : FOOD  |  Escape : CLEAR') # the title

    background = pygame.image.load(bg_image).convert() #this prepares the jpg image

    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (False, False, True): # if right click
                    a, b = pygame.mouse.get_pos()
                    fish_positions.append([a, b])
                    print "fish_positions = ", fish_positions

                if pygame.mouse.get_pressed() == (True,False,False): # if left click
                    c, d = pygame.mouse.get_pos()
                    food_positions.append([c, d])
                    print "food_positions = ", food_positions

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  #THIS WILL CLEAR THE SCREEN
                    food_positions = [] # erases food
                    fish_positions = [] # erases fish

        #screen.fill((0,0,0)) # clears screen/ fills the screen with black
        screen.blit(background, (0,0))      #this keeps redrawing the background
        draw_fishes(fish_positions) # draw fish based on right click
        draw_foods(food_positions) # draw food based on left click
        move_fishes_towards_food(fish_positions, food_positions)
        fps_clock.tick(fps)

        # screen.blit(mouse_cursor,(x,y))     #redraws the mouse cursor image at x,y (cursor position)
        pygame.display.update()  #not sure what this does


def draw_fishes(fish_positions):
    """
    draws every fish, using fish_positions locations

    @param fish_positions
    a list of 2-lists which represent x,y coordinates of the fishes
    """

    for body_coordinate in fish_positions: # n[0] = x, n[1] = y coordinates

        fish_body_coordinates_relative_to_nose = [
            (body_coordinate[0]-90,  body_coordinate[1]+9),
            (body_coordinate[0]-121, body_coordinate[1]+20),
            (body_coordinate[0]-120, body_coordinate[1]-21),
            (body_coordinate[0]-92,  body_coordinate[1]-3),
            (body_coordinate[0]-39,  body_coordinate[1]-29),
            (body_coordinate[0],     body_coordinate[1]),
            (body_coordinate[0]-37,  body_coordinate[1]+24)
        ]

        fish_eye_centerpoint = (body_coordinate[0]-33, body_coordinate[1]-10)
        fish_eye_radius = 7

        screen.lock()
        # draws fish body
        pygame.draw.polygon(screen, BLUE, fish_body_coordinates_relative_to_nose, 0)
        #draws fish eye
        pygame.draw.circle(screen, YELLOW, fish_eye_centerpoint, fish_eye_radius,0)
        screen.unlock()

def draw_foods(food_positions):
    """
    draws all food in food_positions

    @param food_positions
    a list of 2-lists which represent x, y coordinates of the food
    """

    for food_location in food_positions:
        # the '-2' is so that the cursor is in the center of the square, not at the upper left corner. '5' is length, height
        food_square = Rect(food_location[0]-2,food_location[1]-2,5,5)
        screen.lock()
        pygame.draw.rect(screen, WHITE, food_square, 0)
        screen.unlock()

def remove_first_food_from_list(food_positions):
    food_positions = food_positions[1:]
    return food_positions



def move_fishes_towards_food(fish_positions, food_positions):
    """
    Moves each fish towards the food.

    @param fish_positions
    a list of 2-lists which represent x,y coordinates of the fishes

    @param food_positions
    a list of 2-lists which represent x, y coordinates of the food

    @return
    a list of 2-lists which represent x, y coordinates of the food
    """
    # if there are things in food_positions, then there is food on the screen
    if len(food_positions) > 0:
        current_food_position = food_positions[0]
        for fish_position in fish_positions:
            food_x_distance_from_fish = abs(fish_position[0] - current_food_position[0])
            food_y_distance_from_fish = abs(fish_position[1] - current_food_position[1])
            # moves the fish if the fish is farther than fish_move_distance pixels from the food
            #print "\nfood_positions line 156: ", food_positions
            #print "food_positions line 158: ", food_positions
            if food_x_distance_from_fish > fish_move_distance or food_y_distance_from_fish > fish_move_distance:
                # Move the fish towards the food, if it's above the food, move it down,
                # If it's below food, move it up
                for axis in fish_position:
                    if axis > current_food_position[fish_position.index(axis)]:
                        # if fish is below or right, changes the x or y coordinate to move closer to the food
                        fish_position[fish_position.index(axis)] = axis - fish_move_distance
                    else:
                        # if fish is above or left, changes the x or y coordinate to move closer to the food
                        fish_position[fish_position.index(axis)] = axis + fish_move_distance
            else:
                for axis in fish_position:
                    fish_position[fish_position.index(axis)] = current_food_position[fish_position.index(axis)]
                #todo: error on 156. occurs: 2+ fish, when food is supposed to be removed. crashes when fish nose == food coordinate
                food_positions.remove(current_food_position)


                #food_positions = remove_first_food_from_list(food_positions)

                    # makes the closest fish's nose coordinates match the food coordinates ('eating')
                    # removes that food coordinate from the food_positions
                    # this will be for any fish whose position is <= fish_move_distance pixels away.
                    # if any fish is within fish_move_distance pixels of the food, that fish's nose coordinate will match the food coordinate


def test():
    """
    this test moves the fish coordinates toward the food one step (10 pixels).

    @param food_positions
    a list of 2-lists which represent x, y coordinates of the food

    @param fish_positions
    a list of 2-lists which represent x,y coordinates of the fishes
    """

    fishes = [[100,101]] # fish_positions
    foods = [[200,201]]  #food#positions

    move_fishes_towards_food(fishes, foods)

    print "\nresult: fish_positions = ", fishes # [[110,111]]
    print "result: food_positions = ", foods   # [[200,201]]


if __name__ == '__main__': #this allows import of this without automatic code execution
    main()
    #test()




##############################################

##          stamp a ham on mouseclick
##          draw a shark on the page (and make it move towards food)
##              -distance between "nose" point and center of food
##              -move a little each step in the loop
##

#shark = 'shark.png'
#food = 'dsham.png'

#class sharkSprite(pygame.sprite.Sprite):
    
#class foodSprite(pygame.sprite.Sprite):


#foodPos = [] # list of tuples of x,y coordinates of "food"
#fishPos = [] # list of tuples of x,y coordinates of
#Nx,Ny = 0,0 # this is the nose coordinate of the fish, which will draw the rest of the body

#dFood =
#moveList = [] # 3 item tuple: iterator, x pos, y pos
#fishIter = 0 # fish iterator: first fish = 1, second fish = 2, third fish = 3


"""
def remove_food_coordinate(food_positions):
    ---
    Removes one piece of food from the screen.

    @param food_positions
    a list of 2-tuples which represent x, y coordinates of the food

    @return
    returns a new list of food_positions minus the first entry
    ---
    food_positions = food_positions[1:]
    return food_positions


    return

"""
"""
        if event.type == KEYDOWN:
            if event.key = K_RIGHT:
                flip_x = True
            elif event.key = K_LEFT:
                flip_x = False


        new_image = pygame.transform.flip(image, flip_x, False)
"""

"""
def moveFishes(foodPos, fishPos):




    for position in fishPos:




def move_fishes_towards_food(fish_positions, food_position):
    return fish_positions

def test_code():
    fish_positions = [(0, 0), (1, 1), (1, 2)]
    food_position = (3, 4)

    result = move_fishes_towards_food(fish_positions, food_position)
    # Compare result is
    self.assert(result == [(1, 1), (2, 2), (2, 3)])
    self.assert(result == [(1, 1), (2, 2), (2, 3)])
    self.assert(result == [(1, 1), (2, 2), (2, 3)])


    if result == [(1, 1), (2, 2), (2, 3)]:
        good
    else:
        bad

def moveFish():
    if foodPos != []: # do not move fish unless there is food
        for tup in fishPos: # for each fish
            if abs(tup[1] - foodPos[0][1]) > 10 and abs(tup[0] - foodPos[0][0]) > 10: # if fish is above or below food by more than 10
                for coor in tup:
                    if coor > foodPos[0][coor]: # if fishPos x or y is greater than foodPos x or y
                        fishPos.replace(tup[coor], tup[coor] - 10) # moves fish up or right by 10 pixels
                    else: # coor < foodPos[0][coor] # if fishPos x or y is less than foodPos x or y
                        fishPos.replace(tup[coor], tup[coor] + 10) # moves fish down or left by 10 pixels
            else:
"""
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
        #moveFish() # moves fish 10 pixels closer to the the food, up to 10 pixels away -- COMBINE WITH eatFood() TO MAKE moveOrEat()
        # if Nx[n]-xFood[n] > 10 (move distance) pixels, and Ny[n]-yFood[n] != 0, moveFish() # moves all fish along
        # ... moveFish() iterates the first value of foodPos over fishPos, so each fish moves towards the same food.
        # if Nx[n]-xFood[n] < 10 (move distance) pixels, and Ny[n]-yFood[n] == 0, eatFood() # puts a fish on food location
        # possible bug if fish tie.  make it so closest fish (in pixels) wins
        # ... eatFood() iterates

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


