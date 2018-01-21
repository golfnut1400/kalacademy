
'''
Introduction to Programming
Homework 2
Created by: Stan Corpuz
Jan 20, 2018

3.	 (Convert feet into meters) Write a program that reads a number in feet, converts it to meters,
      and displays the result. One foot is 0.305 meters. Here is a sample run:
      Enter a value for feet: 16.5
      16.5 feet is 5.0325 meters

'''


# def feetToMeter():
#     feet = float(input("Enter the number of feet to covert to meters: "))
#     meter = feet * 0.305
#     print()
#     print(feet,"feet is",meter, "meters")
#
# feetToMeter()



'''
Use of while Loop
'''

def feetToMeter():
    while True:
        try:
            feet = float(input("Enter the number of feet to covert to meters: "))
            meter = feet * 0.305
            print()
            print(feet,"feet is",meter, "meters")

        except ValueError:
            print("Oops!  That was no valid number.  Try again... \n")

feetToMeter()
