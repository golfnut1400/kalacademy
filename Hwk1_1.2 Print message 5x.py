# Introduction to Programming
# Homework 1

# 1.2 Display the same message 5 times 'Welcome to Python'

print('--- Message prints 5x using ''* 5 ---')
print('Welcome to Python \n' * 5)  # print string 5x on separate lines using '\n'


print()


# Use of function to print myMessage 5x
print ('--- Use of Function ---')
def message(myMessage):
    count = 0
    while count < 5:    # remember number begins with '0'
        print(myMessage)
        count = count + 1

message('Welcome to Python ')   # calls message function and passes a string




