"""
You just got hired into a new engineering position - congratulations!
The employer required you relocate,so you moved into a new apartment
with a bunch of old typical boring picture frames.
Before you even think about hosting a housewarming party with yournew coworkers,
you might want to decorate your living room with eccentric picture frames that you
can create using your coding skills. You wish to build a machine that prints out a
frame with the provided width, height, and any character as an input.
For example, if you were to build a 4 x 4 frame with the # symbol, your frame would look like:

[["####"], ["# #"], ["# #"], ["####"]]

In this case, for all the enclosed brackets, there should 4 characters printed,
and only the start and end of the bracket should have the # character printed -
the remaining two characters should be two spaces. If the number were five, for example,
we should display the two brackets each started and ending with # symbols and with three spaces in between.

Since you do not own any small photos, you need to make sure that your
machine won't make a frame if the width or height is 3 or less.

"""

def pictureFrame(width, height, character):
    if width <= 3 or height <= 3:
        return "This frame is too small, try again!"
    frame = [character * height]
    for x in range(2):
        frame.append(character * (width - 2))
    frame.append(character * height)
    return frame

print(pictureFrame(4, 5, '*'))
