from graphics import *
dim_x = 1200
dim_y = 800
win = GraphWin('Line', dim_x, dim_y)


def line_dda(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    x,y = p1[0], p1[1]
    if (abs(dy) > abs(dx)):
        steps = dy
    else:
        steps = dx
    
    steps = abs(steps)

    # Incrementation in x and y after each step
    inc_x = dx / steps
    inc_y = dy / steps

    # printing points in screen 
    while (steps):
        steps -= 1
        Point(x, y).draw(win)
        x += inc_x
        y += inc_y

    return

# Optimised ( from both start and end point )
def line_dda_1(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    x,y = p1[0], p1[1]
    end_x, end_y = p2[0], p2[1]
    if (abs(dy) > abs(dx)):
        steps = dy
    else:
        steps = dx
    
    steps = abs(steps)

    # Incrementation in x and y after each step
    inc_x = dx / steps
    inc_y = dy / steps

    # printing points in screen 
    while (steps/2):
        steps -= 1
        Point(x, y).draw(win)
        Point(end_x, end_y).draw(win)
        x += inc_x
        y += inc_y
        end_x -= inc_x
        end_y -= inc_y

    return

line_dda((50,200), (200,50))
line_dda_1((50,250), (200,100))

line_dda((150,400), (600,800))
line_dda_1((200,400), (650,800))
