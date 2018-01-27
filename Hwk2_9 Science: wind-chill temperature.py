'''
Introduction to Programming
Homework 2
Created by: Stan Corpuz
Jan 21, 2018

#Homework 2 9 Science: wind-chill temperature
'''

#Python's program to calculate the Wind Chill Index (WCI)


#CONSTANT
WINDCHILL_OFFSET    = 35.74
WINDCHILL_FACTOR1   = 0.6215
WINDCHILL_FACTOR2   = 35.75
WINDCHILL_FACTOR3   = 0.4275
WINDCHILL_EXP       = 0.16

# function takes the temperature value from user
def windChillIndex():
    temp = float(input("Enter the air temperature in (degrees Farenheit between -58 and 41): "))

    speedMPH = float(input("Enter the wind speed (miles per hour >= 2): "))

#Calculate the WCI
    wci  = WINDCHILL_OFFSET + (WINDCHILL_FACTOR1 * temp) - (WINDCHILL_FACTOR2 * speedMPH ** WINDCHILL_EXP) + (WINDCHILL_FACTOR3 * temp * speedMPH ** WINDCHILL_EXP)
    print("Your Wind Chill Index "'{:.5f}'.format(wci))



windChillIndex()
