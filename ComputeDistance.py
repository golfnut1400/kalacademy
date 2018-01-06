# Enter the first point
x, y = eval(input("Enter x and y for point 1: ")) 
#Enter the second point
x1, y1 = eval(input("Enter x and y for point 2: "))

#compute the distance
distance = ((x1-x)**2 + (y1-y)**2) ** 0.5

print("The distance between the two point is", distance)
