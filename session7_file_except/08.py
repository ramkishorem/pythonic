"""
Exceptional crash landing

Earlier I mentioned something about handling errors without 
letting the program crash.  This will make your programs more 
robust when they encounter bad data, whether it comes from 
innocent mistakes or from malicious attempts to break your
programs. With this skill, you'll make your programs more 
applicable, usable, and stable.

Exceptions are handled with try-except blocks. A try-except block 
asks Python to do something, but it also tells Python what to do 
if an exception(error) is raised.

Instead of tracebacks, which can be confusing for users to read, 
users will see friendly error messages that you write.
"""

try:
    print(1/0)
except:
    print("The computer cannot handle infinity")
# Python throws error when denominator of division is 0
# Output: The computer cannot handle infinity

# Let us see another example which generates a different error
example = {'a':1}

try:
    print(1/2)
    print(example['b'])
except:
    print("The computer cannot handle infinity")
# Output:
# 0.5
# The computer cannot handle infinity
"""In this case the denominator is not 0. So the error message
we show is wrong. We can fix by knowing the Exception names"""

try:
    print(1/2)
    print(example['b'])
except ZeroDivisionError:
    print("The computer cannot handle infinity")
except KeyError:
    print("the dictionary does not contain this key")
# Output:
# 0.5
# the dictionary does not contain this key
