'''Introduction to Programming
Homework 1
Created by: Stan Corpuz
Jan 19, 2018'''

# 1.4 Print a table

# Basically:
#
# the % character informs python it will have to substitute something to a token
# the s character informs python the token will be a string
# the 5 (or whatever number you wish) informs python to pad the string with spaces up to 5 characters.


column1 = ["a",1,2,3,4] # use of list [] containing str and int
column2 = ["a^2",1,4,9,16]
column3 = ["a^3",1,8,27,64]

#zip - Make an iterator that aggregates elements from each of the iterables.
for row in zip(column1, column2, column3):
    print("%-5s %-5s %s" % row) # formatted to a width of 5

