#return the smallest number that can divide into all numbers from 1-20 with no remainder.
#working code, but need to refactor
"""
def is_divisible_by(n, divide_by):
    return n % divide_by == 0


def recurse(n):
    found = True
    for i in range(2, 20):
        if is_divisible_by(n, i):  # this will return true if one is matched, not *all* as is needed
            found = False

    if found:
        return n
    else:
        return recurse(n+1)

print "calculating..."
recurse(20)

"""
#bobby's working code (refactor of mine)
n = 1
target = 1
while n == 1:
    all_mods_are_zero = True
    for i in range(3, 21):
        if target % i != 0:
            all_mods_are_zero = False  # I don't understand how this checks *all* cases and not just one.
            break

    if all_mods_are_zero:
        print "target reached:", target
        n = 0
    else:
        target += 1

 
"""
target = 1
n = 1
print "calculating..."

while n == 1:
    if target % 20 == 0:
        if target % 19 == 0:
            if target % 18 == 0:
                if target % 17 == 0:
                    if target % 16 == 0:
                        if target % 15 == 0:
                            if target % 14 == 0:
                                if target % 13 == 0:
                                    if target % 12 == 0:
                                        if target % 11 == 0:
                                            if target % 10 == 0:
                                                if target % 9 == 0:
                                                    if target % 8 == 0:
                                                        if target % 7 == 0:
                                                            if target % 6 == 0:
                                                                if target % 5 == 0:
                                                                    if target % 4 == 0:
                                                                        if target % 3 == 0:
                                                                            if target % 2 == 0:
                                                                                print "target reached:", target
                                                                                n = 0
                                                                            else:
                                                                                target += 1
                                                                        else:
                                                                            target += 1
                                                                    else:
                                                                        target += 1
                                                                else:
                                                                    target += 1
                                                            else:
                                                                target += 1
                                                        else:
                                                            target += 1
                                                    else:
                                                        target += 1
                                                else:
                                                    target += 1
                                            else:
                                                target += 1
                                        else:
                                            target += 1
                                    else:
                                        target += 1
                                else:
                                    target += 1
                            else:
                                target += 1
                        else:
                            target += 1
                    else:
                        target += 1
                else:
                    target += 1
            else:
                target += 1
        else:
            target += 1
    else:
        target += 1


"""
"""
#nonworking code:

target = 2520
def factor(n):

    global target
    while n > 2:
        if target % n == 0:
            if n == 2:
                print target

            else:
                factor(n-1)
        else:
            target += 1
            n = 20
print "calculating..."
factor(20)
print "done caclulating..."
"""
