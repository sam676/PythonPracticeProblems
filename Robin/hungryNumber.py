"""

Do you remember the joke "Why was 6 afraid of 7? Because 7, 8, 9!" ? 
Well, that joke was wrong. A number can only eat the number to the right of it if the number is SMALLER. 
Once it eats that number, it turns into the sum of itself and that number. 
In our case, only one number will be eating - this number is the first in the array. 
You need to create a function that returns the final array after this number has finished eating.

"""

def hungryNumbers(hungryNums):
    fullNums = []
    for x in range(len(hungryNums)):
        if (x == 0) and (hungryNums[x] > hungryNums[x+1]):
            fullNums.append(hungryNums[0] + hungryNums[x+1])
        else:
            fullNums.append(hungryNums[x])
    return fullNums

#driver
numbers = [2, 7 ,1, 9, 3, 10]
otherNumbers = [7, 2, 1, 10, 8, 4]
print(hungryNumbers(numbers))
print(hungryNumbers(otherNumbers))
