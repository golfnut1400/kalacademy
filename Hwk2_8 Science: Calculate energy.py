'''
Introduction to Programming
Homework 2
Created by: Stan Corpuz
Jan 21, 2018

Homework 2 8 Science calculate energy

8.	(Science: calculate energy) Write a program that calculates the energy needed to heat water
from an initial temperature to a final temperature. Your program should prompt the user to enter
the amount of water in kilograms and the initial and final temperatures of the water. The f
ormula to compute the energy is

Q = M * (finalTemperature – initialTemperature) * 4184
where M is the weight of water in kilograms, temperatures are in degrees Celsius, and energy Q is measured in joules.

Here is a sample run:
Enter the amount of water in kilograms: 55.5
Enter the initial temperature: 3.5
Enter the final temperature: 10.5
The energy needed is 1625484.0



'''


Q = 0 #energy measured in joules

def calculateEnergy(M, initialTemperature, finalTemperature):
    # use of 'global' variable since Q is not declared inside the function
    global Q
    Q = (M * (finalTemperature - initialTemperature)) * 4184
    print("The energy needed is:",Q,'joules')


M = float(input('Enter the amount of water in kilograms: '))
iTemp = float(input('Enter the initial temperature(celcius): '))
eTemp = float(input('Enter the final temperature(celcius): '))

# call function and passes 3 arguments
calculateEnergy(M, iTemp, eTemp)
