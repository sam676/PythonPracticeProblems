"""
Today's question
You are a newbie detective investigating a murder scene in the boardroom
at the Macrosoft Corp. While searching for clues, you discover a red notebook.
Inside of the notebook are long journal entries with inverted messages.
At that moment, you remembered from your profiler father’s advice that
you could stand in front of the mirror to see the messages.
However, you have not slept for 3 days in a row...and haven't showered either.
Because you really don't want to see your face, you decide that you would
rather build an app that can take in a message string and return
the reversed message for you. Now you just need to come up with a
function to build your app - and don't take the shortcut using the "reverse"
method ;)Please reverse this message found in the spooky journal:
.uoy fo lla naht ynapmoc retteb a ekam nac I
.ynapmoc siht ta OEC eht eb ot evresed I

loopsstringsmedium
"""

def reverseMessage(message):
    return(message[::-1])

print(reverseMessage(".uoy fo lla naht ynapmoc retteb a ekam nac I .ynapmoc siht ta OEC eht eb ot evresed I"))
