"""
Line by line

We have been reading a file as a whole. we can also read it 
line by line.
"""
with open('assets/quotes.txt') as quotes_file:
    for quote_line in quotes_file:
        print(quote_line.rstrip())
        # rstrip loses space,newline at end of lines

print()

"""
We can store the lines in a list and use it outside the with block
"""

with open('assets/quotes.txt') as quotes_file:
    quotes = quotes_file.readlines()

print(type(quotes)) # Output: <class 'list'>
print(quotes[1])
# Output:
# "Be yourself; everyone else is already taken." - Oscar Wilde