

# from https://www.youtube.com/watch?v=iDEh-5p_bi0

'''In this Python Pattern Printing Programs video tutorial you will learn to print star '*' in A shape in detail.'''

for row in range(7):    # there are 7 rows
    for col in range(5):
        if ((col==0 or col==4) and row!=0) or ((row==0 or row==3)) and (col>0 and col<4):
            print("A", end="")
        else:
            print(end=" ")
    print()



# printing 'B'
for row in range(7):    # there are 7 rows
    for col in range(5,10):
        if ((col==5 or col==9) and row!=0) or ((row==0 or row==3)) and (col>5 and col<9):
            print("B", end="")
        else:
            print(end=" ")
    print()

print()
for row in range(7):    # there are 7 rows
    for col in range(5):
        if ((col==0 or col==4) and row!=6) or (row==6 and (col>0 and col<4)):
            print("U", end="")
        else:
            print(end=" ")
    print()



