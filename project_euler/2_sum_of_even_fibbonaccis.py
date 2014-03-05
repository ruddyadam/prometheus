fiblist = [1]
def fib(fiblist):
    while fiblist[-1] < 4000000:
        if len(fiblist) == 1:
            fiblist.append(1)
        else:
            fiblist.append(fiblist[-1] + fiblist[-2])
        print fiblist
    sumlist = []
    for n in fiblist:
        if n%2 == 0:
            sumlist.append(n)
    print "sum of even fibbonacci numbers below 4000000 is:", sum(sumlist)

fib(fiblist)
