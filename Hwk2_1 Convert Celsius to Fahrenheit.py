# Introduction to Programming
# Homework 2
# Created by: Stan Corpuz
# Jan 20, 2018

#1 (Convert Celsius to Fahrenheit)



'''1.	(Convert Celsius to Fahrenheit) Write a program that reads a Celsius degree from the console and converts it
to Fahrenheit and displays the result. The formula for the conversion is as follows:

fahrenheit = (9 / 5) * celsius + 32
Here is a sample run of the program:
Enter a degree in Celsius: 43
43 Celsius is 109.4 Fahrenheit
'''



def celsiusToFaharenheit(celsius):

    faharenheit = ((9/5 * celsius) + 32)
    return(faharenheit)

celsius = float(input('Enter a degree in Celsius: '))

# Calls celsiusToFaharenheit functon then prints results in faharenheit
print(celsius, "Celsius is",celsiusToFaharenheit(celsius), "Fahrenheit")



#Use of input within the main() function

# def main():
#     celsius = float(input("What is the Celsius temperature? "))
#     fahrenheit = 9.0 / 5.0  * celsius + 32
#     print (celsius,"Celsius is", fahrenheit, "Fahrenheit.")
#
# main()




