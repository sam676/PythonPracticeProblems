"""
Write a function that, when given a list of integers, 
prints the pair of numbers with the shortest number of 
steps in between. In this case, you can assume that the array of points is 
already sorted. For example, if S = {1, 3, 4, 8, 13, 17, 20} is given, the result will be (3, 4).

"""

def shortestInterval(points):
    minimum = 100000000000000000
    results = []
    for x in range(1, len(points)-1):
        difference = points[x] - points[x-1]
        if (difference <= minimum):
            minimum = difference
            results = [points[x-1], points[x]]
        previous = x
    return results
        


#driver
S = [1, 3, 4, 8, 13, 17, 20]
print(shortestInterval(S))