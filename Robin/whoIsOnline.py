"""

Write a function that returns the number of users who are online in your slack channel. Please include the following features:

1) If nobody is online, return "There is nobody online."

2) If one person is online, return "username online"

3) If there are two people online, return "username and username2 are online

4) If there are more than two people, return "username, username2, and # more are online." So, if there were 6 people total online, you could return "username, username2, and 4 more are online."

ex) whoIsOnline(["user123", "user4"]) ➞ "user123 and user4 are online"

"""

def whoIsOnline(users):
    #no one is online
    if len(users) == 0:
        print("There is nobody online.")
        return
    elif len(users) == 1:
        print("{0} is online".format(users[0]))
    elif len(users) == 2:
        print("{0} and {1} are online".format(users[0], users[1]))
    else:
        print("{0}, {1}, and {2} more are online".format( users[0], users[1], (len(users)-2)))


#driver
whoIsOnline([])
whoIsOnline(["user123"])
whoIsOnline(["user123", "user4"])
whoIsOnline(["user123", "user4", "userp00p"])
whoIsOnline(["user123", "user4", "userp00p", "user456"])
