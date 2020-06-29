"""
For some odd reason, your computer science professor has become obsessed with parentheses - 
she probably spent too much time coding these days... In any case, she wants you to write 
a function that will turn each group of parentheses in a string into separate groups - 
these groups should be balanced.

For example:

group("()()()") ➞ ["()", "()", "()"]

group("((())())(()(()()))") ➞ ["((())())", "(()(()()))"]

"""

def groupParentheses(parentheses):
    left = 0
    right = 0
    string = ""
    newList = []
    for x in parentheses:
        if x == "(":
            left += 1
            string += "("
        else:
            right += 1
            string += ")"
        if left == right:
            newList.append(string) 
            left = 0
            right = 0
            string = ""
    return newList


#driver
testGroup1 = "()()()"
testGroup2 = "((())())(()(()()))"
print(groupParentheses(testGroup1))
print(groupParentheses(testGroup2))
