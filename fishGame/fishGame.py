"""
fishGame.py
Python 2.7.6

user is presented with a window with an underwater background.
use right click to spawn a fish at cursor, left click to spawn food at cursor.
fish swims to food and eats it, then moves to the next food in drop order.
if there is no food, the fish stops.
"""


#todo: KNOWN BUG:   fish will sometimes stop and 'get stuck' when their coordinates match the food.
#                   when a newly spawned fish eats the food, they become 'unstuck'



import pygame, sys
from pygame.locals import *
import random
import math

screenRect = Rect(0,0,640,480)  #sets the screen size
#screenSize = (640, 480)

BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
bg_image = 'aquarium.jpg'
#body_range = [-5,5,1] #number of pixels variation to draw the body
#random_range = 4 #number of pixels variation to draw fish eye

def main(): #the main function
    #!/usr/bin/python2
    pygame.init()  #this initializes pygame

    global background
    global screen

    food_positions = [] # a list of 2-lists containing x,y coordinates of 'food'
    fish_positions = [] # a list of 2-lists containing x,y coordinates of the 'nose' of the fish
    fish_waypoints = [] #not implemented yet
    #list_of_distances_of_fishes_to_foods = []

    body_range = (-15,15) #number of pixels variation to draw the fish body
    eye_range = (-5,5) #number of pixels variation to draw the fish eye
    fish_variation_randints = [] #a list of 14-lists, each item of which will provide variation for each fish body coordinate
    cycle_swim_style = 1

    fps_clock = pygame.time.Clock()  #this is for syncing fps in the game.
    fps = 100 # maximum frames per second (main loops per 1000 milliseconds
    fish_move_distance = 1 # in pixels

    screen = pygame.display.set_mode((screenRect.size),0,32) # this creates the screen
    pygame.display.set_caption('~~Ultimate Fish Game~~ Right Click: FISH | Left Click: FOOD | Escape: CLEAR | SPEED: 1+ / 2- / 3= ') # the title

    background = pygame.image.load(bg_image).convert() #this prepares the jpg image

    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            if event.type == MOUSEBUTTONDOWN:

                # if right click
                if pygame.mouse.get_pressed() == (False, False, True):
                    fish_variation_randints.append(get_randints_for_fish_variation(body_range, eye_range))
                    #print fish_variation_randints
                    a, b = pygame.mouse.get_pos()
                    fish_positions.append([a, b])
                    #print "fish_positions = ", fish_positions

                #if left click
                if pygame.mouse.get_pressed() == (True,False,False):
                    c, d = pygame.mouse.get_pos()
                    food_positions.append([c, d])
                    print "food_positions = ", food_positions

            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:  #THIS WILL CLEAR THE SCREEN
                    food_positions = [] # erases food
                    fish_positions = [] # erases fish

                if event.key == K_1:
                    fps = lower_fps(fps)

                if event.key == K_2:
                    fps = raise_fps(fps)

                if event.key == K_3:
                    fps = 100

                #testing if F4 works for fish creation
                if event.key == K_F4:
                    a, b = pygame.mouse.get_pos()
                    fish_positions.append([a, b])
                    #print "fish_positions = ", fish_positions

                #sets waypoint to mouse position
                if event.key == K_F7:
                    e, f = pygame.mouse.get_pos()
                    fish_waypoints.append([e, f])

                #sets waypoint to random spot on the screen
                if event.key == K_F8:
                    g = random.randrange(2,638,1)
                    h = random.randrange(2,478,1)
                    fish_waypoints.append([g,h])


        #screen.fill((0,0,0)) # clears screen/ fills the screen with black
        screen.blit(background, (0,0))
        draw_fishes(fish_positions, fish_variation_randints)
        draw_foods(food_positions)
        food_positions = any_food_compare_and_remove_from_list(food_positions, fish_positions)

        list_of_distances_of_fishes_to_foods = returns_a_list_of_distances_of_fishes_to_foods(fish_positions, food_positions)

        move_fishes_towards_food(fish_positions, food_positions, fish_move_distance, cycle_swim_style, list_of_distances_of_fishes_to_foods)
        #first_food_compare_and_remove_from_list(food_positions, fish_positions)

        #food_positions = get_that_corn_outta_mah_face(food_positions, fish_positions)
        fps_clock.tick(fps)

        # screen.blit(mouse_cursor,(x,y))     #redraws the mouse cursor image at x,y (cursor position)
        pygame.display.update()  #not sure what this does

def lower_fps(my_fps):
    """
    decreases the fps, decreasing the speed of the fish

    @param my_fps
    int variable

    @return
    int variable
    """
    if my_fps > 49:
        my_fps -= 10
        return my_fps
    else:
        return my_fps

def raise_fps(my_fps):
    """
    increases the fps, increasing the speed of the fish

    @param my_fps
    int variable

    @return
    int variable
    """
    if my_fps < 1001:
        my_fps += 10
        return my_fps
    else:
        return my_fps

def get_randints_for_fish_variation(body_range, eye_range):
    """
    appends a 12-list of random digits within another list.

    @param body_range
    a 2-tuple of intergers

    @param eye_range
    a 2-tuple of intergers

    @return
    a 12-list
    """
    temporary_random_int_list = []
    for fish_variation_number_for_body in range(1,13):
        temporary_random_int_list.append(random.randint(body_range[0], body_range[1]))
    for fish_variation_number_for_eye in range(1,4):
        temporary_random_int_list.append(random.randint(eye_range[0], eye_range[1]))
    #print temporary_int_list
    return temporary_random_int_list

def draw_fishes(fish_positions, fish_variation_randints):
    """
    draws every fish, using fish_positions locations

    @param fish_positions
    a list of 2-lists which represent x,y coordinates of the fishes

    @param fish_variations_randints
    a list of 14-lists
    """

    for body_coordinate in fish_positions: # n[0] = x, n[1] = y coordinates

        variation = fish_variation_randints[fish_positions.index(body_coordinate)]

        fish_body_coordinates_relative_to_nose = [
            (body_coordinate[0]-90 + variation[0],  body_coordinate[1]+9 + variation[1]),
            (body_coordinate[0]-121 + variation[2], body_coordinate[1]+20 + variation[3]),
            (body_coordinate[0]-120 + variation[4], body_coordinate[1]-21 + variation[5]),
            (body_coordinate[0]-92 + variation[6],  body_coordinate[1]-3 + variation[7]),
            (body_coordinate[0]-39 + variation[8],  body_coordinate[1]-29 + variation[9]),
            (body_coordinate[0],                    body_coordinate[1]), #nose, no variation
            (body_coordinate[0]-37 + variation[10], body_coordinate[1]+24 + variation[11])
            ]
        fish_eye_centerpoint = (body_coordinate[0]-33 + variation[12], body_coordinate[1]-10 + variation[13])
        fish_eye_radius = 7 + variation[14]

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

def first_food_compare_and_remove_from_list(food_positions, fish_positions):
    """
    removes the first food in the food_positions list from the board if it matches a fish's position

    @param fish_positions
    a list of 2-lists which represent x,y coordinates of the fishes

    @param food_positions
    a list of 2-lists which represent x, y coordinates of the food

    @return
    a list of 2-lists which represent x, y coordinates of the food
    """
    not_eaten_food = []
    if len(food_positions) > 0 and len(fish_positions) > 0:
        if food_positions[0] in fish_positions:
            not_eaten_food.append(food_positions[1:])
        return not_eaten_food
    else:
        return food_positions

def get_that_corn_outta_mah_face(mah_face, esquelitos_hands):
    """
    a copy of any_food_compare_and_remove_from_list(), with 2 booleans added.
    """
    it_got_slapped_on_the_ground = []
    release_release = True
    two_consecutive_but_ineffective_kicks_to_the_wall = True
    if len(mah_face) > 0 and len(esquelitos_hands) > 0:
        for corn in mah_face:
            if corn not in esquelitos_hands:
                it_got_slapped_on_the_ground.append(corn)
        return it_got_slapped_on_the_ground
    else:
        if release_release:
            if two_consecutive_but_ineffective_kicks_to_the_wall:
                return mah_face

def any_food_compare_and_remove_from_list(food_positions, fish_positions):
    """
    removes food from the board if it matches a fish's position

    @param fish_positions
    a list of 2-lists which represent x,y coordinates of the fishes

    @param food_positions
    a list of 2-lists which represent x, y coordinates of the food

    @return
    a list of 2-lists which represent x, y coordinates of the food
    """
    not_eaten_food = []
    if len(food_positions) > 0 and len(fish_positions) > 0:
        for food_position in food_positions:
            if food_position not in fish_positions:
                not_eaten_food.append(food_position)
        return not_eaten_food
    else:
        return food_positions

def follow_fish_waypoints(fish_waypoints):
    """
    this makes the fish follow the fish waypoints before getting the food.

    @param fish_waypoints
    a list of 2-lists which represent x, y coordinates
    """
    pass

def returns_a_list_of_distances_of_fishes_to_foods(fish_positions, food_positions):
    """
    @param fish_positions
    a list of 2-lists which represent x,y coordinates of the fishes

    @param food_positions
    a list of 2-lists which represent x, y coordinates of the food

    @return
    a list of sub-lists. (length of list is fish_pos items long. length of each sub-list is food_pos items long)
    """

    fishes_to_foods_distances = []
    temporary_holding_list = []
    for fish in fish_positions:
        fish_x = fish[0]
        fish_y = fish[1]
        for food in food_positions:
            food_x = food[0]
            food_y = food[1]
            temporary_holding_list.append(int(math.hypot(abs(fish_x-food_x), abs(fish_y-food_y))))
        fishes_to_foods_distances.append(temporary_holding_list)
        temporary_holding_list = []

    return fishes_to_foods_distances

def index_of_the_first_smallest_integer_in_the_list(list_of_distances_of_fishes_to_foods, fish_positions, fish_position):
    """
    @param fish_position
    an integer. (an iteration item within move_fishes_towards_food)
    this is the index if the fish position in the fish_positions list, which corresponds to a sub-list in list_of_distances_of_fish_to_foods(),
    which will be used to get the return - the index of the smallest value in the list.

    @list_of_distances_of_fish_to_foods
    a list of lists of integers (specifically, the return of list_of_distances_of_fish_to_foods(), which are distances in pixels from each fish to all food)

    @return
    an integer

    """
    closest_food_distance = 10000000 #in pixels
    closest_food_index = 0
    list_of_distances_for_one_fish = list_of_distances_of_fishes_to_foods[fish_positions.index(fish_position)]
    for integer in list_of_distances_for_one_fish:
        if integer < closest_food_distance:
            closest_food_index = list_of_distances_for_one_fish.index(integer)
            closest_food_distance = integer
    return closest_food_index #TODO: THIS WAS INDENTED ON EXTRA TAB, STOPPED EVERYTHING FROM WORKING D:<

def move_fishes_towards_food(fish_positions, food_positions, fish_move_distance, cycle_swim_style, list_of_distances_of_fishes_to_foods):
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
    #follow_fish_waypoints()
    if len(food_positions) > 0:
        for fish_position in fish_positions:
            closest_food_index = index_of_the_first_smallest_integer_in_the_list(list_of_distances_of_fishes_to_foods, fish_positions, fish_position)
            current_food_position = food_positions[closest_food_index]
            #current_food_position = food_positions[0]
            food_x_distance_from_fish = abs(fish_position[0] - current_food_position[0])
            food_y_distance_from_fish = abs(fish_position[1] - current_food_position[1])
            # moves the fish if the fish is farther than 'fish_move_distance' pixels from the food
            if food_x_distance_from_fish > fish_move_distance or food_y_distance_from_fish > fish_move_distance:
                # swim style 1: diagonal to x or y axis towards food, then move along axis to food.
                if cycle_swim_style == 1:
                    # Move the fish towards the food, if it's above the food, move it down,
                    # If it's below food, move it up
                    for axis in fish_position:
                        if axis > current_food_position[fish_position.index(axis)]:
                            # if fish is below or right, changes the x or y coordinate to move closer to the food
                            fish_position[fish_position.index(axis)] = axis - fish_move_distance
                        else:
                            # if fish is above or left, changes the x or y coordinate to move closer to the food
                            fish_position[fish_position.index(axis)] = axis + fish_move_distance
                #swim style 2: only on the lines
                elif cycle_swim_style == 2:
                    #todo: I stopped here, because the current_food_position above needs to change fist, refactor.
                    food_z_distance_from_fish = math.sqrt((food_x_distance_from_fish^2) + (food_y_distance_from_fish^2))



            else:
                for axis in fish_position:
                    #if food is less than 'fish_move_distance' pixels away from fish, fish arrives at food
                    fish_position[fish_position.index(axis)] = current_food_position[fish_position.index(axis)]

def test():
    """
    this test moves the fish coordinates toward the food one step (10 pixels).
    """

    fishes = [[100,101]] # fish_positions
    foods = [[200,201]]  #food_positions

    move_fishes_towards_food(fishes, foods)

    print "\nresult: fish_positions = ", fishes # [[110,111]]
    print "result: food_positions = ", foods   # [[200,201]]

def TESTING_fishes_to_foods_distances():
    fish_positions = [[50,50],[200,200],[500,500]]
    food_positions = [[100,100],[200,200],[300,300]]

    fishes_to_foods_distances = []
    diagonal_distance_from_one_fish_to_food = []
    for fish in fish_positions:
        fish_x = fish[0]
        fish_y = fish[1]
        for food in food_positions:
            food_x = food[0]
            food_y = food[1]
            diagonal_distance_from_one_fish_to_food.append(int(math.hypot(abs(fish_x-food_x), abs(fish_y-food_y))))
        fishes_to_foods_distances.append(diagonal_distance_from_one_fish_to_food) #Todo: this line as well
        diagonal_distance_from_one_fish_to_food = []  #Todo: Bob, is this necessary to separate the "appends" in this loop?

        print "diag", diagonal_distance_from_one_fish_to_food
        print "fishes", fishes_to_foods_distances

    #todo: this does not give the desired output, namely a list of 3 sublists, each for an iteration of a fish over all food.
    #todo:  why are all 3 lists updating? if anything, it should have [[fish1],[fish 1 and 2], [fish 1,2 and 3]]
    #todo: but instead it

        #return fishes_to_foods_distances


if __name__ == '__main__': #this allows import of this  without automatic code execution
    main()
    #test()
    #TESTING_fishes_to_foods_distances()
    #returns_a_list_of_distances_of_fishes_to_foods()




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
        if event.type == KEYDOWN:
            if event.key = K_RIGHT:
                flip_x = True
            elif event.key = K_LEFT:
                flip_x = False


        new_image = pygame.transform.flip(image, flip_x, False)



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


def setFishPos(): # updates the moveList
    # if moveList is empty, create the first entry; fishIter may not be necessary
    moveList.append(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        #moveFish() # moves fish 10 pixels closer to the the food, up to 10 pixels away -- COMBINE WITH eatFood() TO MAKE moveOrEat()
        # if Nx[n]-xFood[n] > 10 (move distance) pixels, and Ny[n]-yFood[n] != 0, moveFish() # moves all fish along
        # ... moveFish() iterates the first value of foodPos over fishPos, so each fish moves towards the same food.
        # if Nx[n]-xFood[n] < 10 (move distance) pixels, and Ny[n]-yFood[n] == 0, eatFood() # puts a fish on food location
        # possible bug if fish tie.  make it so closest fish (in pixels) wins
        # ... eatFood() iterates


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
"""
def get_closest_food(fish_positions, food_positions):

    for each fish, finds out which food is closest.

    @param fish_positions
    a list of 2-lists which represent x,y coordinates of the fishes

    @param food_positions
    a list of 2-lists which represent x, y coordinates of the food

    @return
    an int 2-list from food_positions


    result = []
    iterate each fish x,y over each food x,y,
    calculate the closest food to the fish
    append the closest food to result
    for fish_position in fish_positions:
        fish_x_coordinate = fish_position[0]
        fish_y_coordinate = fish_position[1]
        for food_position in food_positions:
            food_x_coordinate = food_position[0]
            food_y_coordinate = food_position[1]

    return result

1. iterate fish_posiotion in fish_positions over food_positions
2. for 'closest_food(fish_positions, food_positions)
3.



path-to-fish is an else, make normal path the default in a switch/case??  pressing a buttin changes a variable that the fish_path function uses to switch cases.





"""

