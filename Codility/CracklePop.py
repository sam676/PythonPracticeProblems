#CracklePop Program

"""
A program that prints out the numbers 1 to 100 (inclusive). 
If the number is divisible by 3, print Crackle instead of the number. 
If it's divisible by 5, print Pop. If it's divisible by both 3 and 5, print CracklePop.
"""


#Print out numbers 1 to 100 (inclusive)
for n in range (1,101):
	if n % 3 == 0 and n % 5 == 0:
		print("CracklePop")
	elif n % 3 == 0:
		print("Crackle")
	elif n % 5 == 0:
		print("Pop")
	else:
		print n
