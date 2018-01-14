
# Introduction to Programming
# Homework 1
# Created by: Stan Corpuz
# Jan 9, 2018

# 1.13 Draw a cross


import turtle


window = turtle.Screen()
window.bgcolor("green")  # set window color
stan = turtle.Turtle()  # instantiate
stan.pensize(5)
stan.pencolor('red')
stan.shape('turtle')
stan.penup()


stan.goto(-0,-0)  # Start at the middle of the window
stan.left(180)
stan.forward(250)

# draws x axis
stan.right(180)
stan.pendown()
stan.forward(500)

# returns to center
stan.goto(-0,-0)

# draws Y axis
stan.left(90)
stan.penup()
stan.forward(250)
stan.right(180)
stan.pendown()
stan.forward(500)

window.exitonclick()    # window closes only when clicking within the open window
