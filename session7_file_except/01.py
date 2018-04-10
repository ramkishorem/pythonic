"""
We'll learn to work with files so your programs can:
  > Persist data user adds between executions.
  > Analyse huge amount of data by quickly loading them.
  > Convert open form of file to another. (eg: txt -> html)
  > and more..

When you want to work with the information in a text file, 
the first step is to read the file into memory. You can read 
the entire contents of a file, or you can work through the file 
one line at a time.
"""

first_file = open('betty.txt')
contents = first_file.read()
print(contents)
first_file.close()
# Output: prints the content of the file
