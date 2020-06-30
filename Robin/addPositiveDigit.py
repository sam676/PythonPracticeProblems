"""
Beginner programmer John Doe wants to make a program that adds and outputs each positive digit 
entered by the user (range is int). For instance, the result of 5528 is 20 and the result of 6714283 is 31.

"""

def addPositiveDigit(n):
    total = 0
    if n >= 0:
        for x in str(n):
            total += int(x)
    else:
        return "Please enter a positive number!"
    return total

#driver
print(addPositiveDigit(5528))
print(addPositiveDigit(6714283))
print(addPositiveDigit(-6714283))
