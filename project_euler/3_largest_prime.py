#prime factors of 600851475143

#finding a factor: when dividing the large number by a whole number, get a whole number.
#finding a prime: a number that is only divisible by itself and 1.

import math

target = 600851475143


prime_factors = []
number = 1

def get_factors(target, number):
    empty_factor_list = []
    while number < math.sqrt(target):
        if target % 2 != 0:
            if target % number == 0:
                empty_factor_list.append(number)
                empty_factor_list.append(target/number)
        number += 1
    return sorted(empty_factor_list)


for factor in get_factors(target, number):
    templist = []
    if get_factors(factor, number) == [1, factor]:
        prime_factors.append(factor)

factors = get_factors(target, number)
          
print   "Finished! \nThere are", len(factors), "factors for", target, "\nThey are", factors,  "\nThe largest prime factor is:", max(prime_factors)

"""
primes = []
for factor in factors:
    if factor 



new_factors = [factor if factor == min(factors) for factor in factors] 

"""
""""""
