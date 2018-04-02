"""
Loops: the bread-and-butter of programming

A loop is the most common way you can have 
a computer automate repetitive tasks.

Let us analyse the loop we just saw

    "for suspect in suspects:"

When this line is executed first time, Python looks
at the list and assigns the first item to suspect

    suspect = suspects[0] # David

Any statement, any number of statements inside the loop 
will have the value suspect as David. So the print statement
prints

    Next up: David

Since there are no statements inside the loop, Python goes 
back to the for loop line again. It will see if there are 
any more items inside the list to be looped. There are two 
more left. So, Alice is assigned next to suspect.
Print statement prints,

    Next up: Alice

Once again, Python goes back to the for-loop line. One more 
item is left to be looped.
Ben is assigned next to suspect.
Print statement prints,

    Next up: Ben

Back to the loop line, Python will find that there is no 
more item left. So it leaves the loop and proceeds after 
the loop block.
"""