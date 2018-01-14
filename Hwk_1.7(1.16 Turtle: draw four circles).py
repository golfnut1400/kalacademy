
# Introduction to Programming
# Homework 1
# Created by: Stan Corpuz
# Jan 12, 2018

#1.15 Draw 4 circles


import turtle

window = turtle.Screen()
window.setup(width=400, height=400, startx=None, starty=None)   # set screen size to be 400px by 400px, with window set to center of screen


window.title('Turtle: Draw 4 circles')  # set title to the turtle window
window.bgcolor('blue')    # set the window background color



def drawCircle(color, x, y):
    turtle.color(color)
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(50)


drawCircle("black", -50, 50)
drawCircle("yellow", 50, 50)
drawCircle("red", -50, -50)
drawCircle("green", 50, -50)

window.exitonclick()    # window closes only when clicking within the open window
