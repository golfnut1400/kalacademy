
# Introduction to Programming
# Homework 1
# Created by: Stan Corpuz
# Jan 9, 2018

#1.13 Draw a triangle


import turtle

# Triangle #1 playing with different turtle methods


window = turtle.Screen()
window.title('Turtle draw a triangle')  # set title to the turtle window
window.bgcolor("blue")  # set window color
stan = turtle.Turtle()  # instantiate
stan.pensize(5)
stan.pencolor('red')
stan.shape('turtle')
stan.penup()


stan.goto(-0,-0)  # Start at the middle of the window
stan.right(90)  # degree of turn to the right

stan.goto(-0,-200)
stan.left(90)
stan.pendown()
stan.forward(100)
stan.left(120)
stan.forward(200)
stan.left(120)
stan.forward(200)
stan.left(120)
stan.forward(100)
stan.penup()

# Triangle 2 - Simpler drawing of a triangle using a function

def draw_triangle():
    window = turtle.Screen()
    window.bgcolor("green") #background color

    stan = turtle.Turtle()
    stan.goto(-100,-0)
    stan.forward(100)
    stan.left(120)
    stan.forward(100)
    stan.left(120)
    stan.forward(100)
    window.exitonclick() #to exit

draw_triangle() # calls triangle function above



window.exitonclick()    # window closes only when clicking within the open window




