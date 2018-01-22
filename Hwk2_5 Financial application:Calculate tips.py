
'''
# Introduction to Programming
# Homework 2
# Created by: Stan Corpuz
# Jan 20, 2018

5.	(Financial application: calculate tips) Write a program that reads the subtotal and the gratuity rate and computes
    the gratuity and total. For example, if the user enters 10 for the subtotal and 15% for the gratuity rate, the program
    displays 1.5 as the gratuity and 11.5 as the total. Here is a sample run:

    Enter the subtotal and a gratuity rate: 15.69, 15
    The gratuity is 2.35 and the total is 18.04

'''

def tip():
    print()
    tipAmount = float(input('Enter your tip amount '))
    return (tipAmount/100)


tipAmount = 0
myList = [] # use to hold the cost of each purchase
counter = 0

# User can add up to 4 purhace/service items
while counter < 4: #change this to true for infinite (unlimited) loop. also remove counter variables
    num = float(input("Enter cost for each purchase or (q)uit program:"))
    if num == 'q': # entering 'q' will quit the program
        break
    else:
        myList.append(int(num))
    counter +=1

# Adds up the cost purchaces
subTotal = sum(myList)
print ("Your subtotal = " '${:.2f}'.format(subTotal))

# calls th tip() frunction
tip = float((format(tip(),'.2f')))


# Amt of tip from perchaces
graturity = subTotal * tip

print('The graturity is ${:.2f}'.format(graturity), 'and the total is', '${:.2f}'.format(subTotal+graturity))

