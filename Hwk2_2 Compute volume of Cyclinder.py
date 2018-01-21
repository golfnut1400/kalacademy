'''
# Introduction to Programming
# Homework 2
# Created by: Stan Corpuz
# Jan 20, 2018

2.	(Compute the volume of a cylinder) Write a program that reads in the radius and length of a cylinder and computes the
    area and volume using the following formulas:

area = radius * radius * π
volume = area * length
Here is a sample run:

Enter the radius and length of a cylinder: 5.5, 12
The area is 95.0331 The volume is 1140.4
'''

#Exapmle 1

def main():
    celsius = float(input("What is the Celsius temperature? "))
    fahrenheit = 9.0 / 5.0  * celsius + 32
    print (celsius,"Celsius is", fahrenheit, "Fahrenheit.")

main()


#Example 2


import math

def main():
    radius = float(input('Enter the radius: '))
    length = float(input('Enter the length: '))

    area = radius * radius * math.pi
    volume = area * length

    #use of round() function to set decimal to 4 and 1 places
    print('The area is',round(area,4))
    print('The volume', round(volume,1))
main()

