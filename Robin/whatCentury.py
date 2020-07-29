"""
In trying to come up with an insult for your old-fashioned friend (jokingly, of course), 
you ask "What century are you even from?" This made you think about how to convert a year into century format 
- and you have no idea! After doing a little research, you decide to come up with 
a function to save other people from your misery in the future. Please write a function 
that takes in a year and returns the corresponding century. You will only be allowed to 
input years from 1000 - 2010.


How to know a birth century?

Add 1 to the first 2 digits (on the left) of the year of birth, unless it is a year that ends in 00.

Example: 1999 => 19 + 1 = 20 => 20th century.
Example: 2000 => 20 => 20th century.
Example: 2001 => 20 + 1 = 21 => 21st century.

"""

def whatCentury(year):
    result = (year // 100)
    year = str(year)
    if (year[2:] == "00"):
        return result
    else:
        return (result + 1)

#driver
print(whatCentury(2010))
print(whatCentury(2000))
print(whatCentury(1000))
print(whatCentury(1991))
