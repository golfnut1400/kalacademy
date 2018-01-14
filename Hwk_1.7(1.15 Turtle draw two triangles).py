

# Introduction to Programming
# Homework 1
# Created by: Stan Corpuz
# Jan 12, 2018

#1.15 Draw two triangles


import turtle

# Triangle #1 playing with different turtle methods

def draw2triangles():
    window = turtle.Screen()
    window.title('Turtle: draw two triangle')  # set title to the turtle window
    window.bgcolor("green")  # set window color
    stan = turtle.Turtle()  # instantiate
    stan.pensize(5)
    stan.pencolor('blue')
    stan.shape('turtle')
    stan.penup()


    stan.goto(-0,-0)  # Start at the middle of the window
    stan.right(90)  # degree of turn to the right

    stan.goto(-0,-200)
    stan.left(90)
    stan.pendown()
    stan.forward(100)
    stan.left(120)
    stan.forward(400)
    stan.right(120)
    stan.forward(200)
    stan.right(120)
    stan.forward(400)
    stan.left(120)
    stan.forward(100)
    stan.penup()
    window.exitonclick()    # window closes only when clicking within the open window

draw2triangles() # calls triangle function above





