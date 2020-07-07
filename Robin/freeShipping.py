"""

Been doing most of your shopping online? 
It looks like your favorite store is offering a promotion - 
if your total is greater than or equal to $30.00, then you get free shipping! 
Please write a function that returns true if your order is eligible for free shipping and false if it is not.

freeShipping({ "Pens": 4.99, "Notebook": 3.99 }) ➞ false
freeShipping({ "Laptop": 999.99 }) ➞ true


"""

def freeShipping(items):
    total = 0
    for x in items:
        total += items[x] 
    if total >= 30.00:
        return True
    else:
        return False


#driver
print(freeShipping({ "Pens": 4.99, "Notebook": 3.99 }))
print(freeShipping({ "Laptop": 999.99 }))
print(freeShipping({ "Pencil": .99 }))
