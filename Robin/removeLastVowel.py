"""

Do you remember how to write a function that removes the last vowel from each word in a sentence? 
You must only remove the LAST instance of a vowel. For example, "book" would turn into "bok".


"""

def removeLastVowel(word):
    vowels = "aeiou"
    newWord = ""
    count = 0
    for letter in (word[::-1]):
        if letter not in vowels:
            newWord += letter
        else:
            count +=1
            if count > 1:
                newWord += letter
    return (newWord[::-1])
#driver
print(removeLastVowel("apple"))
print(removeLastVowel("book"))
print(removeLastVowel("happy"))
