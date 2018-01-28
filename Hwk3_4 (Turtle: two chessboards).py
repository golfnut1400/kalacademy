

'''
Introduction to Programming
Homework 3
Created by: Stan Corpuz
Jan 27, 2018

Homework 3 Turtle: Two Chessboards
'''






import turtle


def draw_box(t,x,y,size,fill_color):

    t.penup() # no drawing!

    t.goto(x,y) # move the pen to a different position

    t.pendown() # resume drawing



    t.fillcolor(fill_color)

    t.begin_fill()  # Shape drawn after this will be filled with this color!



    for i in range(0,4):

        board.forward(size) # move forward

        board.right(90) # turn pen right 90 degrees



    t.end_fill() # Go ahead and fill the rectangle!





def draw_chess_board(x, y):

    square_color = "black" # first chess board square is black

    start_x = x # starting x position of the chess board

    start_y = y # starting y position of the chess board

    box_size = 30 # pixel size of each square in the chess board

    for i in range(0,8): # 8x8 chess board

        for j in range(0,8):

            draw_box(board,start_x + i * box_size, start_y - j * box_size, box_size, square_color)

            square_color = 'black' if square_color == 'white' else 'white' # toggle after a column

        square_color = 'black' if square_color == 'white' else 'white' # toggle after a row!





board = turtle.Turtle()

#draw_chess_board()
draw_chess_board(-250, 200)
draw_chess_board(25, 200)

turtle.done()
