"""
Project Euler - Problem 3 
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def largestPrime(number):
    largest = 0
    divisor = 2

    while divisor <= number / divisor:
        if number % divisor == 0:
            largest = divisor
            number /= divisor
        else:
            divisor += 1
    
    if largest < number:
        largest = number

    return int(largest)


#driver
print(largestPrime(600851475143))
