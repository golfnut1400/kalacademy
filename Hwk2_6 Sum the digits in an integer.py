'''
Introduction to Programming
Homework 2
Created by: Stan Corpuz
Jan 20, 2018

Homework 2 6 Sum of the digits in an integer

6.	(Sum the digits in an integer) Write a program that reads an integer between 0 and 1000 and adds
    all the digits in the integer. For example, if an integer is 932, the sum of all its digits is 14.
    (Hint: Use the % operator to extract digits, and use the // operator to remove the extracted digit.
    For instance, 932 % 10 = 2 and 932 // 10 = 93.) Here is a sample run:

    Enter a number between 0 and 1000: 999
    The sum of the digits is 27



'''

digits=int(input("Enter a number between 0 and 1000: "))

if digits >=0 and digits <=1000:
    total=0
    while(digits>0):
        # gets the last digit
        digNum=digits%10
        # adds digits
        total=total+digNum
        # //10 removes the extracted digits
        digits=digits//10
    print("The total sum of digits is:",total)
else:
    print("Try Again!")
