#prime factors of 600851475143

#finding a factor: when dividing the large number by a whole number, get a whole number.
#finding a prime: a number that is only divisible by itself and 1.
#hint: only need to search factors up to sqrt(target)

import math

target = 600851475143
prime_factors = []
number = 1

def get_factors(target, number):
    empty_factor_list = []
    while number <= math.sqrt(target):
        if target % 2 != 0:
            if target % number == 0:
                empty_factor_list.append(number)
                empty_factor_list.append(target/number)
        number += 1
    return sorted(empty_factor_list)

factors = get_factors(target, number)

if __name__ == "__main__":
    print "calculating largest prime factor of 600851475143..."

    for factor in get_factors(target, number):
        templist = []
        if get_factors(factor, number) == [1, factor]:
            prime_factors.append(factor)
    
    print "Finished! \nThere are", len(factors), "factors for", target, "\nThey are", factors,  "\nThe largest prime factor is:", max(prime_factors)
