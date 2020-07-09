"""

Some programming languages like Python prefers Pothole case over Camel case.

For instance: in JavaScript, you’d write yellowMonkey but in Python you’d write yellow_monkey. 
In case you forget, you should just build a function where you convert any string in Camel 
case to Pothole case.


"""

def convertCamelCase(convertMe):
    pothole_case = ""
    for x in convertMe:
        if x == x.upper():
            pothole_case += "_"
        pothole_case += x.lower()
    return pothole_case

#driver
thisString = "thisString"
yellowMonkey = "yellowMonkey"
print(convertCamelCase(thisString))
print(convertCamelCase(yellowMonkey))
