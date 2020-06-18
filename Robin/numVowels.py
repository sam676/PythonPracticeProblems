"""
Supercalifragilisticexpialidocious - now you can say it 
backwards which is Dociousaliexpisticfragicalirupus! 
But that's going a bit too far, don't you think? 
This is not a string reversal challenge - did you think it was? 
Instead, can you write a function that returns the number of vowels in a string? 
In particular, the team at Robin REALLY wants to know how many vowels 
are in "supercalifragilisticexpialidocious"!

"""

def numVowels(word):
    vowelCount = {
        'a':0, 
        'e':0, 
        'i':0, 
        'o':0, 
        'u':0
    }
    for letter in word.lower():
        if letter in vowelCount:
            vowelCount[letter] +=  1
    print(vowelCount)


#driver
numVowels("supercAlifragilisticExpiAlidocious")
