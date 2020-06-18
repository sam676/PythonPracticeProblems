"""

Stuck in quarantine...still...and all alone,
you decide to play a game of Scrabble against YOURSELF -
rather, against your shadow. That pesky shadow of yours is known to be
quite the Scrabble ace. In order to make sure that you have the best
chance at winning, you decide to create a function that receives an
array of words. The function should score the words and return an array
of the words (or word) with the highest score. Please use the table below
for reference:

POINTS

A: 1

B: 3

C: 3

D: 2

E: 1

F: 4

G: 2

H: 4

I: 1

J: 8

K: 5

L: 2

M: 3

N: 1

O: 1

P: 3

Q: 10

R: 1

S: 1

T: 1

U: 1

V: 4

W: 4

X: 8

Y: 4

Z: 10

"""

def scrabble(words):
    points = {
        'A': 1,

        'B': 3,

        'C': 3,

        'D': 2,

        'E': 1,

        'F': 4,

        'G': 2,

        'H': 4,

        'I': 1,

        'J': 8,

        'K': 5,

        'L': 2,

        'M': 3,

        'N': 1,

        'O': 1,

        'P': 3,

        'Q': 10,

        'R': 1,

        'S': 1,

        'T': 1,

        'U': 1,

        'V': 4,

        'W': 4,

        'X': 8,

        'Y': 4,

        'Z': 10
        
        }
    scoredWords = dict.fromkeys(words, 0)
    for word in words:
        for letter in word:
            scoredWords[word] += points[letter.upper()]
    return scoredWords

#driver 
print (scrabble(['apple', 'bat', 'cat', 'happy']))
    

    
