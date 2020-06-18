"""
Coding is just like playing an instrument.
If you want to get better, you need to have a solid concept
of even the most basic things! Robin wants to challenge you
to go back to the basics and write a function that determines
if a given string is a palindrome or not. In case you need a
refresher on palindromes: a palindrome is a string that is
read the same front to back and back to front. For example,
words like Mom, Kayak, and noon are palindromes.
Palindromes can also be longer strings made up of multiple words,
such as: "Was it a cat I saw"
"""

def palindrome(string):
    noSpaces = "".join(string.split())
    backwards = noSpaces[::-1]
    return (noSpaces.lower() == backwards.lower())

#driver
print(palindrome("Was it a cat I saw"))
print(palindrome("malayalam"))
