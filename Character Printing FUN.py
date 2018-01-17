
'''
Printing FUN Pattern Character
Created: Scorpuz
Date: 1/15/2018

'''

# Pattern F
for row in range(7):
    for col in range(6):
        if (col==0) or ((row==0 or row==3) and col>0):
            print("*",end="")
        else:
            print(end=" ")
    print()


print()
# Pattern U
for row in range(7):    # there are 7 rows
    for col in range(5):
        if ((col==0 or col==4) and row!=6) or (row==6 and (col>0 and col<4)):
            print("U", end="")
        else:
            print(end=" ")
    print()




print()
# Pattern N
for row in range(6):
    for col in range(6):
        if col==0 or col==5 or (row==col and (col>0 and col<5)):
            print("*",end="")
        else:
            print(end=" ")
    print()
