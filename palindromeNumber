"""
Sheltered at home, you are so bored out of your mind that you start thinking
about palindromes. A palindrome, in our case, is a number that reads the
same in reverse as it reads normally. Robin challenges you to write a
function that returns the closest palindrome to any number of your choice.
If your number is exactly in between two palindromes, return the smaller
number. If the number you chose IS a palindrome, return itself. Have fun!
"""

def palindromeNum(number):
    number = str(number)
    reverse = number
    reverse = reverse[::-1]
    #if the given number is the same going forwards as is backwards
    #return the number
    if str(number) == reverse:
        return(number)
    else:
        #otherwise divide the number in half
        half = len(number) // 2
        #convert the number from an int to a string
        number = str(number)
        #if the length of the number is odd, add one to the legth
        if (len(number) % 2):
            half += 1
            #store the firt half of the number
            start = number[:half]
            #store the seconf half of the number minus the middle number
            end = start[0:half-1]
            #reverse the second half of the number
            end = end[::-1]
            #combine both parts of the number to make a palindrome
            newNumber = start + end
        else:
            #if the number is even, divide it in half
            newNumber = number[:half]
            #reverse the beginning and combine both parts of the number to
            #make a palindrome
            newNumber += newNumber[::-1]
        return(newNumber)
        
#drivers
print(palindromeNum(123456))
print(palindromeNum(1234567))
