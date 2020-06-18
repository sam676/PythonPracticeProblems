"""
*buzz buzz buzz* Flies...again? 
Didn't you just get rid of them this morning? 
In a world like the one seen in Tron, 
you could just write a function to get rid of each "fly" you see. 
Why don't you do the same: write a function that removes each 
"fly" you see in a string, as well as any letter from the word "fly" 
(f, l, or y), just to be safe! For example, 
if you passed in a string like "flyflyfflllgoflyyyyflynefffff", 
it would return the string "gone". 
If there are no "fly"s or traces of "fly"s, return the string 
"No flies here!" Give it a try!

"""

def removeFlies(flyString):
    cleanString = ""
    for letter in flyString.lower():
        if letter != 'f' and letter != 'l' and letter != 'y':
            cleanString += letter
    return (cleanString)

#driver
print(removeFlies("flyflyfflllGoflyyyyflYnefffff"))
