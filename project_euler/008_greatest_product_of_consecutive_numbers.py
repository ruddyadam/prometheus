#http://projecteuler.net/problem=8
#Find the greatest product of five consecutive digits in the 1000-digit number.
"""
string slicing. iterate in string from beginning to end in 5-character slices
make a list of sequences out of those slices (will contain 995)
make a list of products of those sequences
max(list)
"""

string = "73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"

charlist = list(string)
intcharlist = [int(n) for n in charlist]
seqlist = [] 
products = []

# produce a list of 5-item integer sequences starting with each item in thestring up to the 5th character from the end
i = 0
while i < len(intcharlist)-4:
    seqlist.append(intcharlist[i:i+5])
    i += 1

# get the product of every sequence and append it to a the 'products' list    
for sequence in seqlist:
    products.append(sequence[0] * sequence[1] * sequence[2] * sequence[3] * sequence[4])

# print the largest product on the list
print "The largest product of 5 consecutive numbers in the string is:", max(products)


"""
# this was the incorrect to iterate over the entire list, since this loop finds the position of the first item
# in the list that matches whatever 'character' is; it does not give the position of the current item  

for character in newcharlist:
    print charpos
    sequences.append(newcharlist[charpos:charpos+5]) # index will find the *FIRST* item that matches 'charpos' in the list
"""
