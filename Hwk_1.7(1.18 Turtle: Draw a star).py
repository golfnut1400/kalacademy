


# Introduction to Programming
# Homework 1
# Created by: Stan Corpuz
# Jan 12, 2018

#1.18 Draw a star

import turtle

star = turtle.Screen()
star.setup(width=400, height=400, startx=None, starty=None)   # set screen size to be 400px by 400px, with window set to center of screen
star.title('Turtle: Draw a 5 point star')  # set title to the turtle window
star.bgcolor('blue')    #set the window background color


star = turtle.Turtle()
star.goto(-75,0)
star.speed(1)
star.pensize(5)

star.pencolor('red')

for i in range(5): # of sides to draw
    star.forward(150)
    star.right(144)

turtle.done()

#star.exitonclick()    # window closes only when clicking within the open window
