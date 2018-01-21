'''
Introduction to Programming
Homework 2
Created by: Stan Corpuz
Jan 20, 2018

4.	(Convert pounds into kilograms) Write a program that converts pounds into kilograms.
The program prompts the user to enter a value in pounds, converts it to kilograms, and displays the result. One pound is 0.454 kilograms.

Here is a sample run:
Enter a value in pounds: 55.5
55.5 pounds is 25.197 kilograms

'''


'''
Use of while Loop
'''

def poundToKilo():
    while True:
        try:
            pound = float(input("Enter the number of pounds to covert to kilos: "))
            kilo = pound * 0.454
            print()  #newline
            # reference for 'round()' https://docs.python.org/3/library/functions.html?highlight=round#round
            print(pound,"pound is",round(kilo), "kilograms")

        except ValueError:
            print("That was no valid number.  Try again... \n")

poundToKilo()
