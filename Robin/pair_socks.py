"""
While doing laundry, you notice that your socks are all mixed up and you can't tell if you have all matching pairs or not. Write a function that returns the number of sock pairs you find in the pile. Two instances of the same letter, in our case, will represent a sock pair. For example, "ss".

pairs("ammtaxt") --> 3


"""

def pair_socks(laundry):
    total_pairs = 0
    dresser = {}
    for sock in laundry:
        dresser[sock] = 0

    for sock in laundry:
        dresser[sock]+= 1

    for sock in dresser:
        # if (dresser[sock] == 2):
        #     total_pairs += 1
        if (dresser[sock] >= 2):
            total_pairs += (dresser[sock] // 2)
    return total_pairs         


#driver
print(pair_socks("ammtaxtttppp"))