
# Created by: Stan Corpuz
# Jan 13, 2018

#Draw multi Polygons


import turtle
import math


window = turtle.Screen()
window.setup(800, 800, 0, 0)   # set screen size to be 800px by 800px, with window set to center of screen
window.title('Turtle: Draw a polygon')  # set title to the turtle window
window.bgcolor('green')    #set the window background color

poly = turtle.Turtle()  #create a turtle object
poly.shape('turtle')



def drawPolygon (poly, x, y, num_side, radius):
  sideLen = 2 * radius * math.sin (math.pi / num_side)
  angle = 360 / num_side
  poly.penup()
  poly.goto (x, y)
  poly.pendown()
  for iter in range (num_side):
    poly.forward (sideLen)
    poly.left (angle)

def main():


  # draw octagon
  poly.color ('DarkOrchid4')
  drawPolygon (poly, 40, 69.28, 6, 100)
  drawPolygon (poly, -40, -69.28, 6, 100)
  drawPolygon (poly, -80, -9.8, 6, 100)
  drawPolygon (poly, -40, 69.0, 6, 100)
  drawPolygon (poly, 80, 0, 6, 100)

  # persist drawing
  turtle.done()
  poly.exitonclick()    # window closes only when clicking within the open window


main()
