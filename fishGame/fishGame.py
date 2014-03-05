#!/usr/bin/python2
"""
fishGame.py
Python 2.7.6

user is presented with a window with an underwater background.
use right click to spawn a fish at cursor, left click to spawn food at cursor.
fish swims to food and eats it, then moves to the next food in drop order.
if there is no food, the fish stops.
"""


#todo: KNOWN BUG:   fish will sometimes stop and 'get stuck' at some coordinates when attempting to eat food.
#                   when a newly spawned fish eats the food, they become 'unstuck'

#todo: -----------  GAME -------------
#todo:  score - "food eaten total"
#       numbers on fish for how much food they've eaten
#       4 fish to start.
#       the fish will detonate if they touch each other, a fish will detonate if alone, then game over.
#       if a fish eats food, they go faster.
#       a hook a fish at cursor with spacebar to catch it.
#       win scenario:  high score... "food total" when detonation occurs.


import pygame, sys, os
from pygame.locals import *
import random
import math
import json

json_config_location = os.getcwd() +'\config.json'

with open(json_config_location, 'r') as json_config_file:
    settings = json.load(json_config_file)

screenRect = Rect(0,0,640,480)


BLUE = settings["BLUE"]
YELLOW = settings["YELLOW"]
WHITE = settings["WHITE"]
bg_image = settings["bg_image"]

def main():

    pygame.init()

    global background
    global screen

    # A list of 2-lists containing x,y coordinates of 'food'.
    food_positions = settings["food_positions"]

    # A list of 2-lists containing x,y coordinates of the 'nose' of the fish.
    fish_positions = settings["fish_positions"]

    # The special F12 message.
    message = "full_message.txt"
    message_positions = []

    # This toggles the "writing" functionality of F12.
    write_toggle = settings["write_toggle"]

    # The maximum amount of variation in the coordinates of a new fish body from the default fish body.
    maximum_fish_body_variation = settings["maximum_fish_body_variation"]

    # The maximum amount of variation of a new fish eye from the default fish eye.
    maximum_fish_eye_variation = settings["maximum_fish_eye_variation"]

    #a list which will be populated by 14 integers, each integer will provide variation for each fish body coordinate.
    fish_variation_randints = []

    # The selection for the pattern the fish uses to swim to the food.
    cycle_swim_style = settings["cycle_swim_style"]

    fps_clock = pygame.time.Clock()

    # The maximum frames per second (main loops per 1000 milliseconds).
    fps = settings["fps"]

    # The distance in pixels the fish will take each "step".
    fish_move_distance = settings["fish_move_distance"]

    screen = pygame.display.set_mode((screenRect.size),0,32)
    pygame.display.set_caption('~~Ultimate Fish Game~~ Right Click: FISH | Left Click: FOOD | Escape: CLEAR | SPEED: 1+ / 2- / 3= ') # the title

    background = pygame.image.load(bg_image).convert()

    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:

                # On a right click, creates body variation for a fish, and sets fish spawn coordinates.
                if pygame.mouse.get_pressed() == (False, False, True):
                    fish_variation_randints.append(get_randints_for_fish_variation(maximum_fish_body_variation, maximum_fish_eye_variation))
                    a, b = pygame.mouse.get_pos()
                    fish_positions.append([a, b])

                # On a left click, creates food square.
                if pygame.mouse.get_pressed() == (True,False,False):
                    c, d = pygame.mouse.get_pos()
                    food_positions.append([c, d])

            if event.type == KEYDOWN:

                # This will clear fish and food from the screen.
                if event.key == K_ESCAPE:
                    food_positions = []
                    fish_positions = []

                # Pressing "1" will lower Frames Per Second by 10, slowing down the fish.
                if event.key == K_1:
                    fps = lower_fps(fps)

                # Pressing "2" will raise Frames Per Second by 10, speeding up the fish.
                if event.key == K_2:
                    fps = raise_fps(fps)

                # Pressing "3" will set the game speed to the default 100 Frames Per Second.
                if event.key == K_3:
                    fps = 100

                # Pressing "F4" draws a fish at the cursor position, of default size.
                if event.key == K_F4:
                    fish_variation_randints.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
                    a, b = pygame.mouse.get_pos()
                    fish_positions.append([a, b])

                # Pressing "F1" toggles the swim style
                if event.key == K_F1:
                    if cycle_swim_style <= 3:
                        cycle_swim_style += 1
                    else:
                        cycle_swim_style = 1

                # Pressing "F12" toggles the main game loop to allow a message to be written, clears the screen, and loads the message coordinates from a file.
                if event.key == K_F12:
                    if write_toggle == 0:
                        food_positions = []
                        fish_positions = []
                        message_positions = load_a_list_of_tuples_from_a_file(message)
                        write_toggle = 1
                    else:
                        write_toggle = 0

                # Pressing "Backspace" deletes the last food created.
                if event.key == K_BACKSPACE:
                    #todo: make the '+' key add them back in.  i.e., trade removed/readded items to/from another queue list
                    food_positions = food_positions[:-1]
                    message_positions = message_positions[:-1]

        # -- 'normal mode' -- write toggle is 'off'
        if write_toggle == 0:

            screen.blit(background, (0,0))
            draw_fishes(fish_positions, fish_variation_randints, write_toggle)
            draw_foods(food_positions)
            food_positions = any_food_compare_and_remove_from_list(food_positions, fish_positions)
            #food_positions = get_that_corn_outta_mah_face(food_positions, fish_positions)
            list_of_distances_of_fishes_to_foods = returns_a_list_of_distances_of_fishes_to_foods(fish_positions, food_positions)
            move_fishes_towards_food(fish_positions, food_positions, fish_move_distance, cycle_swim_style, list_of_distances_of_fishes_to_foods, write_toggle, message_positions)
            #first_food_compare_and_remove_from_list(food_positions, fish_positions)
            fps_clock.tick(fps)
            # screen.blit(mouse_cursor,(x,y))     #redraws the mouse cursor image at x,y (cursor position)
            pygame.display.update()  #not sure what this does

         #  -- 'surprise write mode' -- this alternate loop is required to allow a the fish to appear to 'write' instead of 'eat'
        else:

            screen.blit(background, (0,0))

            if len(fish_positions) == 0:
                fish_positions = [message_positions[0]]  #fish appears at next food draw location

            if len(fish_variation_randints) == 0:
                fish_variation_randints.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

            draw_fishes(fish_positions, fish_variation_randints, write_toggle)

            if len(fish_positions) > 0 and len(message_positions) > 0:
                for fish_position in fish_positions:
                    if fish_position == message_positions[0]:
                        food_positions.append(message_positions[0])
                        #todo: is the following line problematic?
                        message_positions = message_positions[1:]
            else:
                write_toggle = 0

            draw_foods(food_positions)
            list_of_distances_of_fishes_to_foods = returns_a_list_of_distances_of_fishes_to_foods(fish_positions, food_positions)
            move_fishes_towards_food(fish_positions, message_positions, fish_move_distance, cycle_swim_style, list_of_distances_of_fishes_to_foods, write_toggle, message_positions)
            fps_clock.tick(fps)
            pygame.display.update()

def load_a_list_of_tuples_from_a_file(tuple_txt):
    """
    This will take a string of tuples from a text file and convert it into a list of lists.

    @param tuple_txt
    A string of 2-tuples.

    @return
    A list of lists, each containing 2 items..
    """
    with open(tuple_txt, 'r') as smth_load:
        outputThis = smth_load.read()
        smth_parsed_final = [tuple(int(i) for i in a.strip('()[]').split(',')) for a in outputThis.split('), (')]
        list_of_lists_smth_parsed_final = []
        for n in smth_parsed_final:
            temp_list = []
            for i in n:
                temp_list.append(i)
            list_of_lists_smth_parsed_final.append(temp_list)
        return list_of_lists_smth_parsed_final

def lower_fps(my_fps):
    """
    Decreases the fps, decreasing the speed of the fish.

    @param my_fps
    An integer representing the current frames per second.

    @return
    The new frames per second as integer.
    """
    if my_fps > 49:
        my_fps -= 10
        return my_fps
    else:
        return my_fps

    if my_fps > 49:
        my_fps -= 10
    return my_fps

def raise_fps(my_fps):
    """
    Increases the fps, increasing the speed of the fish.

    @param my_fps
    An integer representing the current frames per second.

    @return
    The new frames per second as integer.
    """
    if my_fps < 1001:
        my_fps += 10
        return my_fps
    else:
        return my_fps

def get_randints_for_fish_variation(maximum_fish_body_variation, maximum_fish_eye_variation):
    """
    Appends a 12-list of random digits within another list.

    @param maximum_fish_body_variation
    A 2-tuple of integers representing the maximum amount of body coordinates variation in pixel distance from the default.

    @param maximum_fish_eye_variation
    A 2-tuple of integers representing the maximum amount of eye radius variation in pixel distance from the default.

    @return
    A list of size 15 representing the actual amount of variation in pixels of fish body and eye coordinates from the default.
    """
    temporary_random_int_list = []
    for fish_variation_number_for_body in range(1,13):
        temporary_random_int_list.append(random.randint(maximum_fish_body_variation[0], maximum_fish_body_variation[1]))
    for fish_variation_number_for_eye in range(1,4):
        temporary_random_int_list.append(random.randint(maximum_fish_eye_variation[0], maximum_fish_eye_variation[1]))
    return temporary_random_int_list

def draw_fishes(fish_positions, fish_variation_randints, write_toggle):
    """
    Draws every fish, using fish_positions locations.

    @param fish_positions
    A list of 2-lists which represent x,y coordinates of the fishes.

    @param fish_variations_randints
    A list of size 15 representing the actual amount of variation in pixels of fish body and eye coordinates from the default.
    """

    for body_coordinate in fish_positions:

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
    Draws all food in food_positions.

    @param food_positions
    A list of 2-item lists which represent x, y coordinates of the food.
    """
    for food_location in food_positions:
        # the '-2' is so that the cursor is in the center of the square, not at the upper left corner. '5' is length, height
        food_square = Rect(food_location[0]-2,food_location[1]-2,5,5)
        screen.lock()
        pygame.draw.rect(screen, WHITE, food_square, 0)
        screen.unlock()

def first_food_compare_and_remove_from_list(food_positions, fish_positions):
    """
    This removes the first food in the food_positions list from the board if it matches a fish's position

    @param fish_positions
    A list of 2-item lists which represent x,y coordinates of the fishes.

    @param food_positions
    A list of 2-item lists which represent x, y coordinates of the food.

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

"""
    if len(food_positions) > 0 and food_positions[0] in fish_positions:
        food_positions.pop(0)
    return food_positions
"""

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
    A list of 2-item lists which represent x,y coordinates of the fishes.

    @param food_positions
    A list of 2-item lists which represent x, y coordinates of the food.

    @return
    A list of 2-item lists which represent x, y coordinates of the food.
    """
    not_eaten_food = []
    if len(food_positions) > 0 and len(fish_positions) > 0:
        for food_position in food_positions:
            if food_position not in fish_positions:
                not_eaten_food.append(food_position)
        return not_eaten_food
    else:
        return food_positions

def returns_a_list_of_distances_of_fishes_to_foods(fish_positions, food_positions):
    """
    @param fish_positions
    A list of 2-item lists which represent x,y coordinates of the fishes.

    @param food_positions
    A list of 2-item lists which represent x, y coordinates of the food.

    @return
    A list of lists representing the distances of all fishes to all foods. (length of list is fish_pos items long. length of each sub-list is food_pos items long)
    """

    fishes_to_foods_distances = []
    for fish in fish_positions:
        temporary_holding_list = []
        fish_x = fish[0]
        fish_y = fish[1]
        for food in food_positions:
            food_x = food[0]
            food_y = food[1]
            temporary_holding_list.append(int(math.hypot(abs(fish_x-food_x), abs(fish_y-food_y))))
        fishes_to_foods_distances.append(temporary_holding_list)

    return fishes_to_foods_distances

def index_of_the_first_smallest_integer_in_the_list(list_of_distances_of_fishes_to_foods, fish_positions, fish_position):
    """
    @param list_of_distances_of_fish_to_foods
    A list of lists of integers (specifically, the return of list_of_distances_of_fish_to_foods(), which are distances in pixels from each fish to all food)

    @param fish_positions
    A list of 2-item lists which represent x,y coordinates of the fishes.

    @param fish_position
    An integer. (an iteration item within move_fishes_towards_food)
    This is the index if the fish position in the fish_positions list, which corresponds to a sub-list in list_of_distances_of_fish_to_foods(),
    which will be used to get the return - the index of the smallest value in the list.

    @return
    An integer representing the closest food to the the fish.
    """
    closest_food_distance = 10000000 #in pixels
    closest_food_index = 0
    list_of_distances_for_one_fish = list_of_distances_of_fishes_to_foods[fish_positions.index(fish_position)]
    for integer in list_of_distances_for_one_fish:
        if integer < closest_food_distance:
            closest_food_index = list_of_distances_for_one_fish.index(integer)
            closest_food_distance = integer
    return closest_food_index #TODO: THIS WAS INDENTED ON EXTRA TAB, STOPPED EVERYTHING FROM WORKING D:<

def move_fishes_towards_food(fish_positions, food_positions, fish_move_distance, cycle_swim_style, list_of_distances_of_fishes_to_foods, write_toggle, message_positions):
    """
    Moves each fish towards the food.

    @param fish_positions
    a list of 2-item lists which represent x,y coordinates of the fishes.

    @param food_positions
    A list of 2-item lists which represent x, y coordinates of the food.

    @param fish_move_distance
    An integer representing the amount the fishes will move with each cycle of the game loop.

    @param cycle_swim_style
    An integer representing the pathing style the fish will take to the target food.

    @param list_of_distances_of_fishes_to_foods
    A list of lists representing the distances of all fishes to all foods. (length of list is fish_pos items long. length of each sub-list is food_pos items long)

    @param write_toggle
    An integer representing the toggle of the main loop sequence.

    @param message_positions
    A list of 2-item lists containing coordinates for the write message.

    @return
    A list of 2-item lists which represent x, y coordinates of the food.
    """

    if len(food_positions) > 0:
        for fish_position in fish_positions:
            if write_toggle == 0 and food_positions > 0:
                closest_food_index = index_of_the_first_smallest_integer_in_the_list(list_of_distances_of_fishes_to_foods, fish_positions, fish_position)
                current_food_position = food_positions[closest_food_index]
            else:
                current_food_position = message_positions[0]
            food_x_distance_from_fish = abs(fish_position[0] - current_food_position[0])
            food_y_distance_from_fish = abs(fish_position[1] - current_food_position[1])

            # Moves the fish if the fish is farther than 'fish_move_distance' pixels from the food
            if food_x_distance_from_fish > fish_move_distance or food_y_distance_from_fish > fish_move_distance:

                # Swim style 1: diagonal to x or y axis towards food, then move along axis to food.
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

                #elif cycle_swim_style == 2:
                    #take distance to closest food, still move 1 "pixel" closer (diagonally)
                    #get coordinates by extrapolating from trajectory and
                    #todo: swim directly towards closest_food_index diagonally
                    #

                #swim style 2: only on the lines
                #elif cycle_swim_style == 3:
                    #todo: swim only two directions, only one time each, on the axes, not diagonally, towards the food
                    # e.g. left to 0 y axis, then down to food.

                #elif cycle_swim_style == 4:
                    #todo: swim in an arc

                #elif cycle_swim_style == 5:
                    #todo: swim in a spiral, where the food is the center of the spiral and the fish is the outer edge
                    #randomize "ovalness" and length of spiral

            else:
                for axis in fish_position:
                    #if food is less than 'fish_move_distance' pixels away from fish, fish arrives at food
                    fish_position[fish_position.index(axis)] = current_food_position[fish_position.index(axis)]

if __name__ == '__main__': #this allows import of this  without automatic code execution
    main()




"""
# for nolstagia: a cryptic function to make a fish swim to food.

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