# Introduction to Programming
# Homework 1
# Created by: Stan Corpuz
# Jan 20, 2018

#1.20 Turtle. Draw a polygon that connects the points (40,-69.28),(-40,-69.28),(-80,-9.8),(-40,69),(40,69),(80,0),(40,-69.28)

# Learn about the different Turtle method. Use of setpos

import turtle


window = turtle.Screen()
window.setup(width=400, height=400, startx=None, starty=None)   # set screen size to be 400px by 400px, with window set to center of screen
window.title('Turtle: Draw a line')  # set title to the turtle window
window.bgcolor('blue')    # set the window background color
line = turtle.Turtle()    # Create a Turtle object
line.shape('arrow')
line.pensize(3)
line.shapesize(1)
line.hideturtle()   #hides turtle
line.pencolor('red')
line.penup()


line.setpos(40,-69.28)
line.pendown()  # sets pendown to draw
line.setpos(-40,-69.28)
line.setpos(-80,-9.8)
line.setpos(-40,69)
line.setpos(40,69)
line.setpos(80,0)
line.setpos(40,-69.28)


window.exitonclick()
