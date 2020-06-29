"""
How are our lovely number people doing today? 
We're going to have an exclusive numbers-only party next week. 
You can bring any type of friends that wear "String" clothes as long as they are real number. 
As we expect the infinite number of numbers to come to the party, 
we should rather build a scanner that will scan every guest and validate whether 
they are a real numbers. If any number brings a fake guest, it will be kicked out of our world! 
Can your team build a special function that will be used in the scanner? 
Please remember, all guests will be wearing string clothes.

For example,

numScanner("2.2") ➞ true

numScanner("1208") ➞ true

numScanner("number") ➞ false

numScanner("0x71e") ➞ false

numScanner("2.5.9") ➞ false

"""

def numScanner(input):
    count = 0
    if input.isdigit():
        return True
    for x in input:
        if x.isalpha():
            return False
        if x == '.':
            count += 1
        if count > 1:
            return False
    return True
        
#driver
print(numScanner("2.2")) 

print(numScanner("1208")) 

print(numScanner("number"))

print(numScanner("0x71e"))

print(numScanner("2.5.9"))
