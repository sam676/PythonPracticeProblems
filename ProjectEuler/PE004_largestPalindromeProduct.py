"""
Largest palindrome product - Problem 4
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def palindromeNumber():
    maxProduct = 0
    for x in range(999, 99, -1):
        for y in range(x, 99, -1):
            product = x * y
            if (product < maxProduct):
                break
            number = product
            reverse = 0
            while (number != 0): 
                reverse = reverse * 10 + number % 10
                number = number // 10
            if ((product == reverse) and (product > maxProduct)):
                maxProduct = product        
    return maxProduct

#driver
print(palindromeNumber())
