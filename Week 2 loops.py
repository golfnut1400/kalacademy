
# Week 2 loops
# While Loop
# For Loop


numberOfStars = eval(input('How many stars to you want to print? '))


for row in range(numberOfStars):

    for col in range(numberOfStars):
        print('*', end=' ') # added a space between the quotes; 'end' means to stay on the same line
    print()
    numberOfStars -= 1  #decrease the stars by 1 as move down the row


