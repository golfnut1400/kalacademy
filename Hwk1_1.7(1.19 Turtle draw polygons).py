
# Introduction to Programming
# Homework 1
# Created by: Stan Corpuz
# Jan 12, 2018

#1.19 Draw a Polygon


import turtle
import math
from shapely import


p1 = geometry.Point(0,0)
p2 = geometry.Point(1,0)
p3 = geometry.Point(1,1)
p4 = geometry.Point(0,1)


pointList = [p1, p2, p3, p4, p1]

poly = geometry.Polygon([[p.x, p.y] for p in pointList])

print(poly.wkt)  # prints: 'POLYGON ((0 0, 1 0, 1 1, 0 1, 0 0))'




#
# window = turtle.Screen()
# window.setup(800, 800, 0, 0)   # set screen size to be 800px by 800px, with window set to center of screen
# window.title('Turtle: Draw a polygon')  # set title to the turtle window
# window.bgcolor('green')    #set the window background color
#
# poly = turtle.Turtle()  #create a turtle object
# poly.shape('turtle')
# poly.color('blue')



#window.exitonclick()    # window closes only when clicking within the open window
