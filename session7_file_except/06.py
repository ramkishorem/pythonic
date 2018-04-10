"""
An intention to Write

We have been reading data from a file. Now we will write 
data in them.
"""

# with open('assets/written.txt') as edit_file:
#     edit_file.write('I am writing through a program')

# Throws error: io.UnsupportedOperation: not writable

"""
This is because by default the file is opened in read-only mode.

If we want to write to a file, we have to set write mode
"""

with open('assets/written.txt','w') as edit_file:
    edit_file.write('I am writing through a program')

"""
When you use the 'w' mode, if the file exists already all the 
information in it will be wiped. You will have a fresh file.

Use append ('a') mode to write to the bottom of the existing file.
"""

with open('assets/written.txt','a') as edit_file:
    edit_file.write('\nThis is the second line')


"""
You may also use read and write ('r+') mode in certain 
circumstances.
"""

# In this mode, you have to read through the existing lines
# before adding new content or you will overwrite
with open('assets/written.txt','r+') as edit_file:
    existing_content = edit_file.read()
    print(existing_content)
    edit_file.write('\nThis is the third line')
