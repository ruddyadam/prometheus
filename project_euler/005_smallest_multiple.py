#the smallest number that can be divided by the numbers 1-20 with no remainder


def smallest_number_with_no_remainder(my_range, target_attempt):

    #if range decreaes to 1, print target number, answer has been found
    if my_range == 1:
        print target_attempt
        
    #if number in my_range is evenly divisible into target number, try next lower number in my_range 
    elif target_attempt % my_range == 0:
        print "decreased range to", my_range -1
        smallest_number_with_no_remainder(my_range-1, target_attempt)
        
        
    #else, increase the target attempt number, to find the smallest one, reset range to 20
    else:
        target_attempt += 1
        print "increased target_attempt to", target_attempt + 1
        smallest_number_with_no_remainder(20, target_attempt+1)
        
        
smallest_number_with_no_remainder(20, 1)
