"""
Here's a fundamental search challenge for you to tackle! 
Binary search algorithms are often efficient, and they work by 
repeatedly dividing the list in half and working with the portion 
that may contain the item being looked for until the possible 
location is narrowed down to just one element. Try giving it a shot!

"""

def binarySearch(array, left, right, item):
    #sort list
    array.sort()
    #base case
    while left <= right:
        #find mid point
        mid = left + (right - left) // 2
        #if the mid point is the item, return the item's position
        if array[mid] == item:
            return mid
        #if the item is greater than the mid point throw away the right side
        elif array[mid] < item:
            left = mid + 1
        #if the item is smaller than the mid point throw away the left side
        else:
            right = mid - 1
    #the item is not in the array
    return None 

#driver
items = [10, 4, 8, 2, 11, 23]

print(binarySearch(items, 0, len(items)-1, 11))
print(binarySearch(items, 0, len(items)-1, 4))