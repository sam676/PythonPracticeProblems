"""
How many mores days are left until you think the COVID-19 pandemic will end?
Why not write a function to tell you so you don't have to calculate it yourself!
Your function should be structured like below - it should take two dates and
return the number of days between the two

function daysToFreedom(date1, date2){}

"""
from datetime import datetime

def daysToFreedom(date1, date2):
    dateFormat = '%m/%d/%Y'
    d1 = datetime.strptime(date1, dateFormat)
    d2 = datetime.strptime(date2, dateFormat)
    difference = d2 - d1
    if '-' in str(difference.days):
        return (difference.days * -1)
    else:
        return difference.days

#driver
d1 = '03/12/2020'
d2 = '06/13/2020'
print(daysToFreedom(d1, d2))

