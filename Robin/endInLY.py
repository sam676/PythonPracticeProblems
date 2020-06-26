"""
An adverb is typically any word that ends in 'ly'. 
Can you write a function that counts the number of words that ends in 'ly'. 
For this problem, even if the word is an adjective, it's still okay to count it as true. 
However, you must not count the word if it starts or contains 'ly' - it MUST be at the end. Happy coding!

"""

def endInLY(wordList):
    count = 0
    for word in wordList:
        if "ly" in word:
            reverse = word[::-1]
            if reverse[0] == "y" and reverse[1] == "l":
                count += 1
    return count




words = ["lysol", "quietly", "truely", "lynx", "happily"]
#driver
print(endInLY(words))

