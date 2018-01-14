'''
Introduction to Programming
Homework 1
Created by: Stan Corpuz
Jan 14, 2018


REFERENCES
https://en.wikibooks.org/wiki/Mathematics_with_Python_and_Ruby/Fractions_in_Python
https://docs.python.org/3/library/fractions.html?highlight=fraction#module-fractions
'''



#1.7 Approximate Pi

# Use of the 'fraction' module
from fractions import *

a = Fraction(1,3)
b = Fraction(1,5)
c = Fraction(1,7)
d = Fraction(1,9)
e = Fraction(1/11)
f = Fraction(1/13)
g = Fraction(1/15)

x = 4 * (1 - (a+b) - (c+d) - (e))
print("Value of Pi is: ",float(x))
print()
print()
x = 4 * (1 - (a+b) - (c+d) - (e+f) - g)
print(("Part 2 Value of Pi is: ", float(x)))
