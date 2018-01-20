
# Introduction to Programming
# Homework 1
# Created by: Stan Corpuz
# Jan 12, 2018

#1.17 Draw a 'red' line connecting two points (-39,48) and (50,-50)

# Learn about the different Turtle method

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

# sets pair of coordinates then prints coordinates
line.setpos(-39,49)
line.write('(-39,49)',font=("Arial", 15, "normal"))  # object to be written to the TurtleScreen

line.pendown()  # sets pendown to draw

line.setpos(50,-50)
line.write('(50,50)',font=("Arial", 15, "normal"))   #object to be written to the TurtleScreen
# print(line.pos()) # prints the position


window.exitonclick()    # window closes only when clicking within the open window
