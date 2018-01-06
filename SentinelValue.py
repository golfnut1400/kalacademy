data = eval(input("Enter an integer. The program ends if it is 0."))
sum = 0
while data != 0:
    sum += data
    data = eval(input("Enter an integer. The program ends if it is 0."))

print("The sum is", sum)
