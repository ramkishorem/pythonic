"""
Copy a List

How could we copy a list?
"""

yesterday_starting_5 = ['Charlotte','Merlin','Fiona',
    'Eli','Sara']

"""
we are making only one change for today.
So it is a good idea to change only that on a copy list
"""

today_starting_5 = yesterday_starting_5
today_starting_5[2] = 'Rudolph'
print(today_starting_5)
# Output: ['Charlotte', 'Merlin', 'Rudolph', 'Eli', 'Sara']
print(yesterday_starting_5)
# Output: ['Charlotte', 'Merlin', 'Rudolph', 'Eli', 'Sara']

"""
oh no! Changing today's list also changes yesterday's list.

In programming terms, both variables are pointing to the same 
location on the memory.

We want our copy to be truly a copy. So what can we do?

Could we do it with the slicing feature?
"""

yesterday_starting_5 = ['Charlotte','Merlin','Fiona',
    'Eli','Sara']
today_starting_5 = yesterday_starting_5[:] # same as [0:-1]
today_starting_5[2] = 'Rudolph'
print(today_starting_5)
# Output: ['Charlotte', 'Merlin', 'Rudolph', 'Eli', 'Sara']
print(yesterday_starting_5)
# Output: ['Charlotte', 'Merlin', 'Fiona', 'Eli', 'Sara']

"""
Now they are two separate lists pointing to different 
locations on the memory.
"""