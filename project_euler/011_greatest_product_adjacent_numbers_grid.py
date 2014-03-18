# http://projecteuler.net/problem=11
# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20 x 20 grid?

grid = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 \
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 \
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 \
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 \
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 \
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 \
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 \
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 \
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 \
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 \
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 \
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 \
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 \
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 \
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 \
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 \
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 \
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 \
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 \
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"

"""
-----------------------------
"JUST WORKING THIGS OUT" AREA
-----------------------------
diagonal down right:
for each line in horizontal_lines_list, between line and line + 3:
    item = 0
    for position,number in enumerate(line):
        grid_vertical_lines_list[position].append(number)

for each line in the grid:
create 17 lists in one list

newlist[firstlist].append(gridlineslist[firstline][firstitem])
newlist[firstlist].append(gridlineslist[secondline][secondlitem])
newlist[firstlist].append(gridlineslist[thirdline][thirditem])
newlist[firstlist].append(gridlineslist[fourthline][fourthitem])
newlist[secondlist].append(gridlineslist[firstline][fifthitem])

a,b,c, = 0,0,0
newlist = []
for line in gridlist:
    for item in line:
        while item < 17
            if c = 3:
                b += 1
                c = 0
                newlist[b].append(gridlineslist[c][c])
            else:
                newlist[b].append(gridlineslist[c][c])



output should be:
list1 = 0,0;1,1;2,2;3,3
list2 = 0,1;1,2;2,3;3,4


17 starting points per line
n = 0
i = 0
this_list[i].append(line_list[n][n]):
n += 1
i += 1

"""

gridlist = grid.split()
gridlist = [int(n) for n in gridlist]


# make each horizontal line in the grid into a list, all of which are contained in a list.
grid_horizontal_lines_list = []
for number in range(0, len(gridlist), 20):
    grid_horizontal_lines_list.append(gridlist[number:number+20])

grid_vertical_lines_list = [[] for x in range(20)]
item_position = 0
for line in grid_horizontal_lines_list:
    for position,number in enumerate(line):
        grid_vertical_lines_list[position].append(number)

grid_diagonal_down_right_list = [[] for x in range(17)]
"""for line in grid_horizontal_lines_list:
    for position,number in enumerate(line):
        grid_diagonal_down_right_list[position]
"""

# this currently only works for one line.  Need to add empty lists for all items.
#for lines 1-17, not 18-20  <--implement

for line in grid_horizontal_lines_list:
    #b, c = 0, 0
    if line != grid_horizontal_lines_list[17] or line != grid_horizontal_lines_list[18] or line != grid_horizontal_lines_list[19]:
        for position, number in enumerate(line):
            if b < 17:
                print position
                print "c=",c
                print "b=",b
                print grid_diagonal_down_right_list
                if c == 3:
                    grid_diagonal_down_right_list[b].append(grid_horizontal_lines_list[c][b+c])
                    b += 1
                    c = 0
                else:
                    grid_diagonal_down_right_list[b].append(grid_horizontal_lines_list[c][b+c])
                    c += 1


#print grid_horizontal_lines_list
#print grid_vertical_lines_list
print grid_diagonal_down_right_list


def largest_product(a_list_of_20_lists):
    product_list = []
    seqlist = []

    for individual_list in a_list_of_20_lists:
        for position, number in enumerate(individual_list):
            if position <= len(individual_list)-4:
                seqlist.append(individual_list[position:position+4])
        #print seqlist
        for sequence in seqlist:
            product = reduce((lambda x,y: x*y), sequence)
            product_list.append(product)
        #print newlist
        #print max(newlist)
    print max(product_list) 
    return max(product_list)


"""
def product_horizontal(a_list_of_20_lists):
    


    vert_list = [[] for x in range(20)]
"""

if __name__ == "__main__":
    largest_product(grid_horizontal_lines_list),"\n"
    largest_product(grid_vertical_lines_list),"\n"
    largest_product(grid_diagonal_down_right_list)   
    
    
    
