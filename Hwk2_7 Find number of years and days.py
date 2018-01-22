'''
Introduction to Programming
Homework 2
Created by: Stan Corpuz
Jan 21, 2018

Homework 2 7 Find number of years and days by entering the number of minutes



'''
# this function will calculate the number of years and
# remaining days when entering a large number of minutes
def minToYearsDays():
    #User to enter minutes
    minutes = int(input("Enter number of minutes: "))

# number of minutes in a year
    years = int(minutes / 525600)

# remaining minutes
    remainingMinutes = int(minutes % 525600)

# 1440 is the number of minutes in 1 day
    day = int(remainingMinutes /1440)

# prints out the value in years and the remaining days
    print()
    print(minutes,"minutes is approximately",format(years), "years and", day, "days.")

# calls the function
minToYearsDays()
