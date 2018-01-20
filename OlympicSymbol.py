import turtle

window = turtle.Screen()
window.bgcolor("purple")    # set the window background color



def drawCircle(color, x, y):
    turtle.color(color)
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(45)



drawCircle("blue", -110, -25)
drawCircle("black", 0, -25)
drawCircle("red", 110, -25)
drawCircle("yellow", -55, -75)
drawCircle("green", 55, -75)

window.exitonclick()    # window closes only when clicking within the open window


