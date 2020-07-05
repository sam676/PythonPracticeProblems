"""
Time for something short and sweet - please write a function that removes the last vowel from each word in a sentence. 
Only remove the LAST instance of a vowel. For example, "moon" would turn into "mon".

"""

def removeFirstVowel(word):
    reverseWord = word[::-1]
    newWord = []
    newWordStr = ""
    count = 0
    for x in reverseWord:
        newWord += x
        if x in ("aeiou"):
            count += 1
            if count == 1:
                newWord.pop()
    for x in newWord:
        newWordStr += x 
    return newWordStr[::-1]




#driver
print(removeFirstVowel("moon"))
