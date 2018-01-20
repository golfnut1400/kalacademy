
'''
Printing FUN Pattern Character
Created: Scorpuz
Date: 1/15/2018

https://www.youtube.com/watch?v=xzzg4Q7ykDU

'''

i=0
j=4

# Pattern X
for row in range(5):
    for col in range(5):
        if row==i and col==j:     #prints star at row 0 and column 4
            print("*",end="")
        # decrement i (row) value by 1
            i = i + 1
        # increase j (column) value + 1
            j = j - 1

        elif row==col:  # the value of row and column are the same
            print("*",end="")
        else:
            print(end=" ")
    print()
