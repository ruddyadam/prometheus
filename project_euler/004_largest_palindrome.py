#largest palindrome of the product of 2 3-digit numbers.
# could be 4,5, or 6 digits
# if string == reverse(string), append to list.
# print max(sorted(list))

number1 = range(100,999)
number2 = range(100,999)
palindromes = []

for numbera in number1:
    for numberb in number2:
        product = numbera * numberb
        if str(product) == str(product)[::-1]:
            palindromes.append(product)
print "There are", len(palindromes), "palindromes."
print max(palindromes), "is the biggest one."




def palindrome(number):
    

