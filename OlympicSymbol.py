import turtle

turtle.pensize(5)
def drawCircle(color, x, y):
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(45)


drawCircle("blue", -110, -25)
drawCircle("black", 0, -25)
drawCircle("red", 110, -25)
drawCircle("yellow", -55, -75)
drawCircle("green", 55, -75)


turtle.done()
