"""
Closing is critical

You have to absolutely close the file or the data in it could 
be corrupted. The issue here is not just that you have to remember 
to close it. If an error occurs after opening the file and before 
closing it, the program will crash without closing the file.

In the later part of the chapter, we will learn how to handle 
errors without letting the program crash.

To stop worrying about closing a file, we can use the with 
statement.
"""

# The with statement magically closes the file
# when all the lines inside it are executed 
# or even if an error occurs. Convenient, isn't it?!
with open('betty.txt') as first_file:
    contents = first_file.read()
    print(contents)
    # Don't have to close the file manually

# Output: prints the content of the file
    