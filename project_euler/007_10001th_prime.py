#http://projecteuler.net/problem=7
#What is the 10001st prime number?

#each target factored and checked if it is prime, then target is iterated once (repeat until while loop is satisfied)
#factoring - get all factors of each target, by dividing each of 1 to the sqrt(target) into target to see if % == 0
#if the only factor is 1, then it is prime

import math

list_of_found_primes = []
factor_this_number = 2
factor_number_attempted = 1


def is_prime(factor_this_number):
    """
    This returns True if factor_this_number is prime.

    @param factor_this_number
    An integer which will be factored and tested to see if it is prime.

    @return
    boolean (True or False)
    """
    
    range_of_factoring_attempts = []
    list_of_all_factors_for_a_number = []

    # range of numbers to use for factoring
    range_of_factoring_attempts = range(1,int(math.sqrt(factor_this_number))+1)

    # appends the number used for factoring to list_of_all_factors_for_a_number if it is a factor
    for attempt in range_of_factoring_attempts:
        if factor_this_number % attempt == 0:
            list_of_all_factors_for_a_number.append(attempt)

    #if the list only includes "1" (will be length of 1), factor_this_number is a prime, so return True.
    if len(list_of_all_factors_for_a_number) == 1:
        return True
    else:
        return False

if __name__ == "__main__": 
    print "Calculating 10001st prime..." 
    
    while len(list_of_found_primes) < 10001:
        if is_prime(factor_this_number):
            list_of_found_primes.append(factor_this_number)
        factor_this_number += 1

    print "Finished! The 10001st prime is:", list_of_found_primes[-1]
