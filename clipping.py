from graphics import *
dim_x = 400
dim_y = 400
win = GraphWin('Line Clipping', dim_x, dim_y)


# Region Codes
INSIDE = 0
TOP = 0b0001
BOTTOM = 0b0010
LEFT = 0b0100
RIGHT = 0b1000

# Accepting Region
max_x = 300
min_x = 100
max_y = 350
min_y = 80
acceptedReg = Rectangle(Point(min_x,min_y), Point(max_x,max_y))
acceptedReg.setFill('green')
acceptedReg.draw(win)

def getCode(point):
    code = INSIDE
    if point.x < min_x:
        code |= LEFT
    elif point.x > max_x:
        code |= RIGHT
    if point.y < min_y:
        code |= TOP
    elif point.y > max_y:
        code |= BOTTOM

    return code

def lineClip(p1,p2):
    c1 = getCode(p1)
    c2 = getCode(p2)
    accept = False

    while True:
        # If both points are inside
        if c1 == 0 and c2 == 0:
            accept = True
            break
        # If both are outside and in same region, so no point on the line which
        # will be inside the region
        elif (c1 & c2) != 0:
            break

        # Some segment lying inside
        else:
            if c1 != 0:
                c_out = c1
            else:
                c_out = c2

            # Finding and replacing intersection point
            if c_out & TOP:
                y = min_y
                x = p1.x + (p2.x - p1.x) * ( y - p1.y) / (p2.y - p1.y)
            elif c_out & BOTTOM:
                y = max_y
                x = p1.x + (p2.x - p1.x) * ( y - p1.y) / (p2.y - p1.y)
            elif c_out & LEFT:
                x = min_x
                y = p1.y + (p2.y - p1.y) * (x - p1.x) / (p2.x - p1.x)
            elif c_out & RIGHT:
                x = max_x
                y = p1.y + (p2.y - p1.y) * (x - p1.x) / (p2.x - p1.x)

            if c_out == c1:
                p1.x = x
                p1.y = y
                c1 = getCode(p1)
            else:
                p2.x = x
                p2.y = y
                c2 = getCode(p2)

    if (accept):
        print("Line Accepted from (%.2f, %.2f) to (%.2f, %.2f)" % (p1.x, p1.y, p2.x, p2.y))
        return 1
    else:
        print("Line rejected")


p1 = Point(180, 200)
p2 = Point(320, 280)
l = Line(p1,p2)
l.setOutline('green')
l.setWidth(4)
l.draw(win)

if (lineClip(p1,p2)):
    l = Line(p1,p2)
    l.setOutline('red')
    l.setWidth(4)
    l.draw(win)


p1 = Point(40, 200)
p2 = Point(200, 40)
l = Line(p1,p2)
l.setOutline('green')
l.setWidth(4)
l.draw(win)

if (lineClip(p1,p2)):
    l = Line(p1,p2)
    l.setOutline('red')
    l.setWidth(4)
    l.draw(win)


p1 = Point(250, 380)
p2 = Point(390, 320)
l = Line(p1,p2)
l.setOutline('green')
l.setWidth(4)
l.draw(win)

if (lineClip(p1,p2)):
    l = Line(p1,p2)
    l.setOutline('red')
    l.setWidth(4)
    l.draw(win)

