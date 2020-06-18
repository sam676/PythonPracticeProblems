"""
Having no coffee left in the house, you run out to grab some,
hastily leaving your wallet behind. You come to this realization
after the barista hands over your Ristretto, and pull out some
loose change from your pocket. Embarrassed, you go home empty-handed
and start on a function to save you next time. Your function will accept a
total amount due and an array that represents the change in your pocket,
and holds values in this order: pennies, nickels, dimes, quarters.
For example, if you provide this array: [1,2,3,4], it means that
the contents in your pocket consist of one penny, two nickels,
three dimes, and four quarters. If you have enough change to cover your
order, the function will return true. Otherwise, it'll return false.
Good luck!
"""

def looseChange(array, cost):
    pennies = array[0]
    nickels = array [1]
    dimes = array [2]
    quarters = array [3]

    pennies = pennies * .01
    nickels = nickels * .05
    dimes = dimes * .10
    quarters = quarters * .25

    pocketChange = pennies + nickels + dimes + quarters
    
    return(pocketChange >= cost)


print(looseChange([1,2,3,4], 2.75))
