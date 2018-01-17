# Introduction to Programming
# Homework 1
# Created by: Stan Corpuz
# Jan 16, 2018

#1.13 Display a Pattern - FUN


'''
I needed help on this. After an exhaustive search how I would join each characters, I reached out to the Community
in StackOverflow

See https://stackoverflow.com/questions/48276660/print-pattern-fun-using-python

'''

# create a 'F' function. Use '.join' string method inside of a list [ ]
def pattern_f():
    return [
        ''.join([
            'F' if (col == 0 or col == 1 or row == 0 or row ==2) else ' '
            for col in range(7)]) for row in range(5)
    ]

# create a 'U' function
def pattern_u():
    return [
        ''.join([
            'U' if ((col==0 or col==6) and row<3) or (row==3 and (col==1 or col==5)) or (row==4 and col>1 and col<5) else ' '
            for col in range(7)]) for row in range(5)
    ]

# create a 'N' function
def pattern_n():
    return [
        ''.join([
            'N' if (col==0 or col==1 or col==6 or col==7) or (row==col-1) else ' '
            for col in range(8)]) for row in range(5)
    ]


##separate printing:
for string in pattern_f():
    print(string)
print()

for string in pattern_u():
    print(string)
print()

for string in pattern_n():
    print(string)
print()

##combining. calling functions above
for f,u,n in zip(pattern_f(), pattern_u(), pattern_n()):
    print(f,u,n)
