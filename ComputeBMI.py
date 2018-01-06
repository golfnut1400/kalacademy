#Promt the user to enter weight in pounds
weight = eval(input("Enter weight in pounds: "))

height = eval(input("Enter height in inches: "))

KILOGRAMS_PER_POUND = 0.45359237 #Constant
METERS_PER_INCH = 0.0254 #Constant

#Compute BMI
weightInKg = weight * KILOGRAMS_PER_POUND
heightInMt = height * METERS_PER_INCH

bmi = weightInKg / (heightInMt ** 2)

#Dsplay result
print("BMI is", format(bmi, ".2f"))
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
