"""
Have you heard about bubble sort? 
Bubble sort is a simple sorting algorithm. 
This sorting algorithm is comparison-based. 
Each pair of adjacent elements are compared and are swapped 
if they are not in order. This is a frequently asked level 1 
question asked by FAANG. Before you get a call from one of them, 
why not practice it today? Please implement bubble sort and explain 
when this algorithm is least suitable and why.

"""


def bubbleSort(bubbles):
    n = len(bubbles)

    for x in range(n-1):
        for y in range(n-x-1):
            if bubbles[y] > bubbles[y+1]:
                bubbles[y], bubbles[y+1] = bubbles[y+1], bubbles[y]

    return bubbles


#driver
testArray = [20, 2, 10, 34, 1, 45, 32]
print(bubbleSort(testArray))
