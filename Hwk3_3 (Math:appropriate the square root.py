


'''
Introduction to Programming
Homework 3
Created by: Stan Corpuz
Jan 27, 2018

Homework 3 Math: Appropriate the square root
'''


number = abs(float(input("Calculate square root of? ")))
lassGuess = abs(float(input("Initial guess? ")))

epsilon = 0.0001

while True:
    difference = lassGuess**2 - number
    print('{} : {}'.format(round(lassGuess, 4), round(difference, 4)))
    if abs(difference) <= epsilon:
        break
    lassGuess = \
        (lassGuess + (number / lassGuess) / 2.0)
