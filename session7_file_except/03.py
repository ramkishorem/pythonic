"""
The path of the File

In our previous example the text file is located in the same 
folder as the Python file. if the file is located in a different
folder, we can either use a relative path or an absolute path.

Let us create a folder 'assets' in the folder that contains 
our python files.
"""

with open('assets/quotes.txt') as quotes_file:
    print(quotes_file.read())
