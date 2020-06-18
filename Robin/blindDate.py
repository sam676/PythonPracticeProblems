
"""
Spring is here and your friend calls to see if you are interested in meeting
someone for a blind date next month. You have been a loner for
so long - solo for 3 years - and even gained 30 pounds.
You are determined to meet the person looking your best,
so you decide to cut meals and do intensive cardio.
You want to track how often your daily caloric intake is lower
than the day before and daily hours spent excercising exceeds
those from the previous day. If so, you will mark it as a success day.
Create a function that returns the total number of success days.
"""

def successfulDays(days):
    successfulDays = 0
    for x in range (1, len(days)):
        day = days[x]
        dayBefore = days[x-1]
        if day[0] < dayBefore[0]:
            if day[1] > dayBefore[1]:
                successfulDays +=1
    return successfulDays
            
    



listOfDays = [[2000, 2], [1899, 4], [2000, 5], [1000, 6], [1000, 6]]
print(successfulDays(listOfDays))
