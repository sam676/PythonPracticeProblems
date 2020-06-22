"""
Largest palindrome product - Problem 4
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def palindromeNumber():
    product = 0
    palindrome = 0
    for x in range(1000):
        for y in range(1000):
            product = x * y
            reverse = str(product)[::-1]
            if product == int(reverse):
                palindrome = product
    return palindrome

#driver
print(palindromeNumber())
