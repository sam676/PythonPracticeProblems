"""

Have you heard about balanced words? 
If a word is balanced, the sum of the values on 
the left-hand side of the word is equal to the sum
 of the values on the right-hand side. Each letter's 
 value comes from its position in the alphabet 
 (a=1, b=2, etc.) and can be summed to determine the left and 
 right hand sums. If a word has an odd number of characters, 
 the middle character should be ignored. Can you write a function
that determines whether or not a word is balanced?

"""

def balancedWords(word):
    alphabet = {
        'a' : 1,
        'b' : 2,
        'c' : 3,
        'd' : 4,
        'e' : 5,
        'f' : 6,
        'g' : 7,
        'h' : 8,
        'i' : 9,
        'j' : 10,
        'k' : 11,
        'l' : 12,
        'm' : 13,
        'n' : 14,
        'o' : 15,
        'p' : 16,
        'q' : 17,
        'r' : 18,
        's' : 19,
        't' : 20,
        'u' : 21,
        'v' : 22,
        'w' : 23,
        'x' : 24,
        'y' : 25,
        'z' : 26
    }
   
    word = word.lower()
    half = len(word) // 2
    end = word[half:]
    start = word[:(half)]
    startScore = 0
    endScore = 0

    if ((len(word)) % 2 != 0):
        end = word[half+1:]

    print("start:" + start + " end: " + end)

    for letter in start:
        startScore += alphabet[letter]
    
    for letter in end:
        endScore += alphabet[letter]
    
    return (startScore == endScore)

#driver
print(balancedWords("teswSet"))
print(balancedWords("tesSet"))
