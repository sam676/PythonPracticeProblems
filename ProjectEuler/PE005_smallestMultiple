"""
Smallest multiple - Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?

"""

def smallestMultiple():
    count = 2520
    x = 20
    while count:
        if count % x == 0:
            x -=1
            if x == 1:
                return (count)
        else:
            count += 1
            x = 20

#driver
print(smallestMultiple())
