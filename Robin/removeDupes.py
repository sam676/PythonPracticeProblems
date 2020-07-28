"""

Can you write a function that takes an array of values and remove all duplicate elements in the array? 
Make sure to return the array with only the unique values remaining.

"""

def removeDupes(thisArray):
    newArray = []
    for item in range(len(thisArray)):
        if thisArray[item] in thisArray[item+1:]:
            continue
        else:
            newArray.append(thisArray[item])
    return newArray


#driver
list = [4, 1, 2 ,4, 5, 6, 2]
print(removeDupes(list))
