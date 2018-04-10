"""
try or else

You can execute a block of code conditionally if the statements
inside the try block did not throw any error using 'else:' block
"""
example = {'a':1}

try:
    print(1/2)
    print(example['a'])
except ZeroDivisionError:
    print("The computer cannot handle infinity")
except KeyError:
    print("the dictionary does not contain this key")
else:
    print("No errors found. Phew!")

# Output:
# 0.5
# 1
# No errors found. Phew!