
# Introduction to Programming
# Homework 1
# Created by: Stan Corpuz
# Jan 15, 2018

#1.15 Draw a clock

'''
Design Requirements
1. Draw a circle - DONE
2. Display text hours for 3, 6, 9, 12 - DONE
3. Display text '9:15:00' @ 6 oclock - DONE
4. Display hour hand pointing to 9:00   - DONE
5. Display minute hand pointing to 3:00 - DONE
'''


import turtle

window = turtle.Screen()
window.setup(width=800, height=800, startx=None, starty=None)   # set screen size to be 400px by 400px, with window set to center of screen


window.title('Turtle: Draw a clock set for 9:15:00')  # set title to the turtle window
window.bgcolor('blue')    # set the window background color

# function to draw the circle
def drawCircle(color):
    turtle.color(color)
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(0,-200) # x & y ---- set to -200 b/c radius is set to 200 to have circle in middle of screen
    turtle.pendown()
    turtle.circle(200) # radius of the circle

drawCircle("red")   #calls the draw function and passes 'red' the color of the stanp line


def displayHours():
    turtle.penup()
    turtle.setposition(0,-185)
    turtle.write('6',font=("Arial", 18, "normal"))  #display 6:00 o'clock

    #display 3:00 o'clock
    turtle.setposition(180,-5)
    turtle.write('3',font=("Arial", 18, "normal"))

    #display 12:00 o'clock
    turtle.setposition(5,175)
    turtle.write('12',font=("Arial", 18, "normal"))

        #display 9:00 o'clock
    turtle.setposition(-180,-5)
    turtle.write('9',font=("Arial", 18, "normal"))

displayHours()


# Display text '9:15:00' @ 6 o'clock

def displayTime(time):
    turtle.setposition(-25,-230)
    turtle.write(time,font=("Arial", 18, "normal"))  #display 6:00 o'clock

displayTime('9:15:00' )



# Display hands of clock
def clockHands ():

    turtle.setposition(0,0) # x & y ---- set to middle of screen
    turtle.pensize(3)
    turtle.pencolor('black')
    turtle.pendown()
    turtle.forward(135)
    turtle.left(180)
    turtle.forward(135)
    turtle.right(15)
    turtle.forward(120)

clockHands()


window.exitonclick()    # window closes only when clicking within the open window
