"""
A stack is the appropriate data structure for keeping the parentheses.
Starting with an empty stack, process the parenthesis strings from left to right.
If a symbol is an opening parenthesis, push it on the stack
as a signal that a corresponding closing symbol needs to appear later.
If, on the other hand, a symbol is a closing parenthesis, pop the stack.
As long as it is possible to pop the stack to match every closing symbol, the parentheses remain balanced.
If at any time there is no opening symbol on the stack to match a closing symbol,
the string is not balanced properly. At the end of the string, when all symbols have been processed, the stack should be empty.

"""

#HOW TO BALANCE PARENTHESIS

def parChecker(symbolString):
    #this stack is actually a list
    stack = []
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            stack.append(symbol)
        else:
            if is_empty(stack):
                balanced = False
            else:
                stack.pop()

        index = index + 1

    if balanced and is_empty(stack):
        return True
    else:
        return False

    
#check if something is empty
def is_empty(any_structure):
    if any_structure:
        return False
    else:
        return True

#test some parenthesis
print(parChecker('((()))'))
print(parChecker('(()'))
