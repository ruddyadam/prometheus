#difference between the sum of the squares and the square of the sum of numbers 1-100

range_list = range(1,101)

sum_of_squares = sum([n**2 for n in range_list])
square_of_sum  = sum(range_list)**2

difference = abs(sum_of_squares - square_of_sum)

print "diffeence is:", difference
