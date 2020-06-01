"""
You're at an in-person interview for a software engineering
role that you applied to last week. The interview starts off
as expected, until the hiring manager asks you this:
"If I give you any two numbers and ask you to add them together,
subtract one from the other, multiply them, or divide one from the other,
could you do it?" You pause at first, because you aren't a math genius.
But then you realize something - this is a technical interview!
You could just write a function that receives two numbers,
an operator ( +, -, x, or / ) and returns the correct answer.
Right? Let's ace this interview! Don't forget, dividing by 0 is an
illegal operation, so make sure to return a message when that case appears.
"""

def operation(num1, op, num2):
    if ((num1 == 0 or num2 == 0) and (op == '/')):
        return("You can't devide by 0! Please enter a different number.")
    elif (op == '+'):
        return num1 + num2
    elif(op == '-'):
        return (num1 - num2)
    elif(op == '*'):
        return (num1 * num2)
    elif(op == '/'):
        return (num1 / num2)
    elif(op == '%'):
        return (num1 % num2)
    else:
        return "invalid syntax"
        

print(operation(3, '*', 3))

    
