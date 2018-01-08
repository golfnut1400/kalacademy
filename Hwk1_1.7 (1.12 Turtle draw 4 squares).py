

# Introduction to Programming
# Homework 1

# 1.12 Draw four squares in the middle of the screen


import turtle


window = turtle.Screen()
window.bgcolor("green")  # set window color
stan = turtle.Turtle()  # instantiate
stan.pensize(5)
stan.shape('turtle')
stan.down()

# creates red square
stan.color("red")
stan.forward(150)
stan.left(90)
stan.forward(150)
stan.left(90)
stan.forward(150)
stan.left(90)
stan.forward(150)
stan.left(90)

# creates yellow square
stan.right(180)
stan.color("yellow")
stan.forward(150)
stan.right(90)
stan.forward(150)
stan.right(90)
stan.forward(150)
stan.right(90)
stan.penup()
stan.forward(150)

# creates black square
stan.color("black")
stan.pendown()
stan.forward(150)
stan.left(90)
stan.forward(150)
stan.left(90)
stan.forward(150)
stan.penup()
stan.left(90)
stan.forward(300)

# creates blue square
stan.color("blue")
stan.pendown()
stan.left(90)
stan.forward(150)
stan.left(90)
stan.forward(150)
stan.penup()
stan.left(90)
stan.forward(150) # returns to center of square

window.exitonclick()    # window closes only when clicking within the open window
