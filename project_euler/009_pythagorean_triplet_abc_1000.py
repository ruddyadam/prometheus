# http://projecteuler.net/problem=9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

"""
iterate range of 1-999 for a,b, and c
test: a**2 + b**2 == c**2

for all combinations where a < b < c and a + b + c == 1000:
    if a**2 + b**2 == c**2:
        return a,b,c

does a+b+c = 1000?  if yes:
is a < b < c?  if yes:
does a**2 + b**2 == c**2?  If yes:
print a*b*c
"""

range_a = range(1,1000)
range_b = range(1,1000)
range_c = range(1,1000)

for a in range_a:
    for b in range_b:
        for c in range_c:
            if a + b + c == 1000:
                if a < b < c:
                    if a**2 + b**2 == c**2:
                        print "a*b*c =", a * b * c
                
