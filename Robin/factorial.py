"""
Do you know what a factorial of a number is?
You can get the factorial of a number by multiplying all the numbers less
than or equal to that number. As an example, 5! (5 factorial),
is equal to 5 X 4 X 3 X 2 X 1 = 120. Would you please write a solution
for Robin that returns the factorial of that number?
"""


def factorial(number):
    return (1 if (number==1 or number==0) else number * factorial(number-1))

print(factorial(5))
