"""

Thanos believes that in order to balance the program, 
half of the elements in the list should be randomly deleted.
Write an Infinity Gauntlet program that randomly deletes and returns 
half of the elements in the input list when Thanos bounces a finger 
(when running the program).(Since it is randomly deleted, the output value 
must be different every time even if the input value is the same)

Input example: [2, 3, 1, 6, 5, 7]

Output example 1: [2, 5, 7]

Output example 2: [3, 6, 5]


"""
import random

def randomDelete(inputList):
    half = int(len(inputList) / 2)
    return random.sample(inputList, half)

#driver
input = [2, 3, 1, 6, 5, 7]
print(randomDelete(input))
print(randomDelete(input))
