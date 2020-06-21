"""
Robin team recently interviewed a former software engineer at Amazon and 
was able to get some of the actual interview questions asked in the last 5 years.

You are given an array of [j1, j2, j3, j4, j5, jn …, k1, k2, k3, k4, k5, kn], 
how would you arrange the given array to [j1, k1, j2, k2, …]?

"""

def shuffleArray(array):
    midpoint = len(array) // 2
    array1 = array[:midpoint]
    array2 = array[midpoint:]
    newArray= []
    for item in range(midpoint):
        newArray.append(array1[item])
        newArray.append(array2[item])
    return newArray

#driver
print(shuffleArray(['j1', 'j2', 'j3', 'j4', 'j5', 'k1', 'k2', 'k3', 'k4', 'k5']))
