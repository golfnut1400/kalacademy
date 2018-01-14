import turtle

painter = turtle.Turtle()

painter.pencolor("blue")

for i in range(50):
    painter.forward(50)
    painter.left(123) # Let's go counterclockwise this time

painter.pencolor("red")
for i in range(50):
    painter.forward(100)
    painter.left(123)

turtle.done()

#
# import turtle
#
# painter2 = turtle.Turtle()
#
# painter2.pencolor("#32D486")
# painter2.forward(30)
#
# painter2.pencolor("#D6305F")
# painter2.forward(30)
