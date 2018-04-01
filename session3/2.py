"""
What's at the end?

To get item from end of the list without knowing its 
length use negative indexing.
"""
scores = [34, 47, 52, 29, 35]
print(scores[-1])

# Output:
# 35

"""
                   [34, 47, 52, 29, 35]
positive indices <- 0   1   2   3   4
negative indices   -5  -4  -3  -2  -1 <-

So [-1] gets you the last value. [-2], the one before 
the last.
"""