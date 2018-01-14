# Prompt the user to enter weight in pounds


weight = eval(input('Enter weight in pounds: '))

height = eval(input('Enter height in inches: '))


#Constant
KILOGRAM_PER_POUND = 0.45359237
METERS_PER_INCH = 0.00254


weightInKg = weight * KILOGRAM_PER_POUND
heightInMeters = height * METERS_PER_INCH

bmi = weightInKg / (heightInMeters ** 2)

print('BMI is', format(bmi,'.2f'))  #use of 'format'

if bmi < 18.5:
    print('You are underweight')

elif bmi < 25:
    print('You are normal')

elif bmi < 30:
    print('Overweight')

else:
    print('Obese')
