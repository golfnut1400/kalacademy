import turtle

smart = turtle.Turtle()

# Loop 4 times. Everything I want to repeat is
# *indented* by four spaces.
for i in range(4):
    smart.forward(50)
    smart.right(90)

# This isn't indented, so we aren't repeating it.
#turtle.done()


print("start test")

for i in range(4):
    print(i)
    print("test")

print("end test 1")
print()


for banana in range(20):
    print(banana)
    print(banana * 2)
