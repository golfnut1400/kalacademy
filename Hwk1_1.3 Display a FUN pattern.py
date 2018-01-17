
'''
Printing FUN Pattern Character
Created: Scorpuz
Date: 1/15/2018

'''

#Pattern F
for row in range(5):
    for col in range(7):
        if (col==0 or col==1) or ((row==0 or row==2)):
            print("F",end="")
        else:
            print(end=" ")
    print()
print()


#Pattern U
for row in range(5):    # there are 5 rows
    for col in range(7): # 7 columns
        if ((col==0 or col==6) and row<3) or (row==3 and (col==1 or col==5)) or (row==4 and col>1 and col<5):
            print("U", end="")
        else:
            print(end=" ")
    print()

print()

print()
# Pattern N
for row in range(5):
    for col in range(9):
        if (col==0 or col==1 or col==6 or col==7) or (row==col-1): #and (col>0 and col<5)):
            print("N",end="")
        else:
            print(end=" ")
    print()



