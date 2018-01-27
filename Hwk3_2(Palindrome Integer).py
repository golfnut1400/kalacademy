
'''
Introduction to Programming
Homework 3
Created by: Stan Corpuz
Jan 27, 2018

#Homework 3 Palindrome Integer

2.	(Palindrome integer) Write the functions with the following headers:
# Return the reversal of an integer, e.g. reverse(456) returns # 654
def reverse(number):

# Return true if number is a palindrome
def isPalindrome(number):

Use the reverse function to implement isPalindrome. A number is a palindrome if its reversal is the same as itself. Write a test program that prompts the user to enter an integer and reports whether the integer is a palindrome.



'''

# Python Program to Reverse a Number using While loop


Reverse = 0
# Function to reverse an interger
def reverse(Number):
    while(Number > 0):
        global Reverse
        Reminder = Number %10
        Reverse = (Reverse *10) + Reminder
        Number = Number //10
    # This print() is a just a check point for me
    print("\n Reverse of entered number is = %d" %Reverse)
    print()

    #Calls isPalidrome() function and passing the
    #reverse integer of users input
    isPalidrone(Reverse)


# Function checks if the reverse number is a palidrome
def isPalidrone(Number):
    temp=Number
    rev=0
    while(Number>0):
        dig=Number%10
        rev=rev*10+dig
        Number=Number//10
    if(temp==rev):
        print("The number is a palindrome!")
    else:
        print("The number isn't a palindrome!")


Number = int(input("Please Enter any Number: "))
# call the reverse() function and passes the argument
reverse(Number)
