"""
You've heard about Magic Squares, right? 
A magic square is one big square split into separate squares 
(usually it is nine separate squares, but can be more), each containing a unique number. 
Each horizontal, vertical, and diagonal row MUST add up to the same number 
in order for it to be considered a magic square.

Now, it's up to you to write a function that accepts a two-dimensional 
array and checks if it is a magic square or not.

Examples:

isMagic([
  [6, 1, 8],
  [7, 5, 3],
  [2, 9, 4]
]) ➞ true


isMagic([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]) ➞ false

"""

def isMagic(array):
    magic =  True
    sumEach = []
    rowNumber = 0
    colNumber = 0
    for row in range (len(array)):
        for column in range (len(array)):
            rowNumber += array[row][column]
            colNumber += array[column][row]
        sumEach.append(rowNumber)
        sumEach.append(colNumber)
        rowNumber = 0
        colNumber = 0
    for x in range(1, len(sumEach)):
        if sumEach[x] != sumEach[x-1] :
            magic = False
    return magic

#driver
print(isMagic([
  [6, 1, 8],
  [7, 5, 3],
  [2, 9, 4]
]))

print(isMagic([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]))