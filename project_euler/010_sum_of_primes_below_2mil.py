# http://projecteuler.net/problem=10
# Find the sum of all the primes below two million.

import math

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

    print "Finding all primes below 2,000,000... (will update every 500,000)"
    is_this_a_prime = 2
    prime_list = []
    
    while is_this_a_prime < 2000000:
        if is_prime(is_this_a_prime):
            prime_list.append(is_this_a_prime)
        is_this_a_prime += 1
            
        if is_this_a_prime == 500000:
            print "Found", len(prime_list), "primes below 500,000..."
        if is_this_a_prime == 1000000:
            print "Found", len(prime_list), "primes below 1,000,000..."
        if is_this_a_prime == 1500000:
            print "Found", len(prime_list), "primes below 1,500,000..."
    print "Finished! Found all primes below 2,000,000! \nThe sum of these", len(prime_list), "primes is:", sum(prime_list)
