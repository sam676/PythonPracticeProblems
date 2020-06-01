"""

You've been quarantined and have become addicted to online shopping
and start hoarding ramen. Much to your surprise, you discover that your
favorite online marketplace is not secure and displays your credit card
details in plain text. Being the good samaritan that you are, you decide
to write a function for them that takes in a credit card number and
returns a string that replaces all but the last four digits with stars,
like this: "************1111". Make sure that the number of stars matches
with the exact number of digits being replaced.

"""

def star(CCNum):
    newNum = list(CCNum)
    for x in range(len(CCNum)-4):
        newNum[x] = '*'
    CCNum = ''.join(newNum)
    return CCNum

print(star("2349204938274"))
    
