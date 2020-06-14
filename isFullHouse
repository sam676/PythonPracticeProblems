"""
Your friends have invited you to play a virtual game of poker!
How exciting...until you realize that you know nothing about Poker.
Don't worry, this Robin challenge will at least help you figure out if
you or your friends have a Full House. A Full House is a hand of 5 cards
that have one pair of cards and one three of a kind. Let's write a function
that takes in an array of 5 cards and tells us if the hand is a full house
or not!

isFullHouse(["K", "K", "A", "K", "A"] ) should return true

isFullHouse(["A","J","10","3","3"]) should return false

"""


def isFullHouse(cards):
    count = {}
    three = False
    two = False
    for card in cards:
        count[card] = 0
    for card in cards:
        count[card] = count.get(card) + 1
    for number in count:
        if count.get(number) == 3:
            three = True
        if count.get(number) == 2:
            two = True
    return(three and two)

#driver
print(isFullHouse(["K", "K", "A", "K", "A"]))
print(isFullHouse(["A","J","10","3","3"]))
print(isFullHouse(["A","A","A","3","3"]))
        
    
