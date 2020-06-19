"""
What's in the box!? Let's check first if there is actually something IN 
the box before we figure out WHAT it is...

Check if the asterisk is inside of the box. 
The function you write must return true only 
if the asterisk is INSIDE - not if it is anywhere else on or 
outside of the box.

For example:

inBox([
  "####",
  "#* #",
  "#  #",
  "####"
]) ➞ true

inBox([
  "*####",
  "# #",
  "#  #*",
  "####"
]) ➞ false

"""

def inBox(box):
    inside = False
    for line in box:
        for x in range(len(line)-1):
          left = line[x-1]
          right = line[x+1]
          if left == '#' and line[x] == '*' and right == ' ':
              inside = True
          if left == ' ' and line[x] == '*' and right == '#':
              inside = True
    return inside

#driver
print(inBox([
  "####",
  "#* #",
  "#  #",
  "####"
]))

print(inBox([
  "*####",
  "# #",
  "#  #*",
  "####"
]))
