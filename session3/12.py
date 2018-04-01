"""
After loop and indentation
"""

suspects = ['David','Alice','Ben']
for suspect in suspects:
    print('Next up: {}'.format(suspect))
    print('{} questioned'.format(suspect))
print('You may all go home. But don\'t leave down.')

# Output:
# Next up: David
# David questioned
# Next up: Alice
# Alice questioned
# Next up: Ben
# Ben questioned
# You may all go home. But don't leave down.

"""
To mark the end of the loop, you have to move indentation 
back to where 'for' statement started.

If you see the third print statement printed multiple times,
it is inside the for loop.

If you see IndentationError, there is an indentation issue 
around the mentioned line.

Try creating these issues now and get familiar with them.
"""