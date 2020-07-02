"""

It looks like you just became a freelancer and snagged your first client. 
Unfortunately, they came to you with NO design and NO idea on what colors 
they want to use. Why don't you come up with a function that returns a random hexadecimal 
color code so you don't have to think about it either.


"""

import random

def colorGenerator():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

#driver
print(colorGenerator())