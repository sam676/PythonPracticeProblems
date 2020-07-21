"""
You and your friend go out to eat. You order dinner and she orders dessert. 
You decide to split the bill - you pay for the food items and she pays only for the dessert items.

If you have two arrays, one with the type of dishes ordered and one with the corresponding price, 
create a function that returns an array where the first element is the amount that YOU pay and the 
second element is that amount that YOUR FRIEND pays.

ex)

splitTheBill(["D", "D", "F", "D"], [1, 1, 3, 2]) ==> [3, 4]

"""

def splitTheBill(dishes, price):
    you = 0
    friend = 0
    for item in range(len(dishes)):
        if dishes[item] == "D":
            friend += price[item]
        else:
            you += price[item]
    return [you, friend]
            
#driver
print(splitTheBill(["D", "D", "F", "D"], [1, 1, 3, 2]))
