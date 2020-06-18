"""

Anagrams are words that contain the exact same letters in the same quantity.
Robin challenges you to write a function that accepts two words and returns true if they are anagrams.
BONUS: write the function so that it can receive any number of words and returns true if all of them are anagrams of each other.
"""


def anagram(word1, word2):
    if (sorted(word1) == sorted(word2)):
        return True
    else:
        return False
    
print(anagram('word', 'drow'))
print(anagram('word1', 'word'))


def anagram2(list):
    anagram = True
    for word1 in list:
        for word2 in list:
            if (sorted(word1) != sorted(word2)):
                anagram = False

    return anagram

list = ['word', 'drow','word1', 'word']

print("anagram2: ", anagram2(list))
