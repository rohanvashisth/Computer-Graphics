from graphics import *
dim_x = 400
dim_y = 400
win = GraphWin('Polygon Clipping', dim_x, dim_y)

# Accepting Region
max_x = 300
min_x = 100
max_y = 350
min_y = 80
acceptedReg = Rectangle(Point(min_x,min_y), Point(max_x,max_y))
acceptedReg.setFill('green')
acceptedReg.draw(win)

def polyClip( polygon ):
    currPoly = polygon
    result = []

    # Left Clipping
    for i in range(len(currPoly)):
        if currPoly[i-1].x < min_x:
            if currPoly[i].x < min_x:
                continue
            else:
                x = min_x
                y = currPoly[i-1].y + ( currPoly[i].y - currPoly[i-1].y ) * ( x - currPoly[i-1].x ) / ( currPoly[i].x - currPoly[i-1].x )
                result.append(Point(x,y))
                result.append(currPoly[i])
        else:
            if currPoly[i].x < min_x:
                x = min_x
                y = currPoly[i-1].y + ( currPoly[i].y - currPoly[i-1].y ) * ( x - currPoly[i-1].x ) / ( currPoly[i].x - currPoly[i-1].x )
                result.append(Point(x,y))
            else:
                result.append(currPoly[i])

    currPoly = result
    result = []

    # Top Clipping
    for i in range(len(currPoly)):
        if currPoly[i-1].y < min_y:
            if currPoly[i].y < min_y:
                continue
            else:
                y = min_y
                x = currPoly[i-1].x + ( currPoly[i].x - currPoly[i-1].x ) * ( y - currPoly[i-1].y ) / ( currPoly[i].y - currPoly[i-1].y )
                result.append(Point(x,y))
                result.append(currPoly[i])
        else:
            if currPoly[i].y < min_y:
                y = min_y
                x = currPoly[i-1].x + ( currPoly[i].x - currPoly[i-1].x ) * ( y - currPoly[i-1].y ) / ( currPoly[i].y - currPoly[i-1].y )
                result.append(Point(x,y))
            else:
                result.append(currPoly[i])

    currPoly = result
    result = []

    # Right Clipping
    for i in range(len(currPoly)):
        if currPoly[i-1].x > max_x:
            if currPoly[i].x > max_x:
                continue
            else:
                x = max_x
                y = currPoly[i-1].y + ( currPoly[i].y - currPoly[i-1].y ) * ( x - currPoly[i-1].x ) / ( currPoly[i].x - currPoly[i-1].x )
                result.append(Point(x,y))
                result.append(currPoly[i])
        else:
            if currPoly[i].x > max_x:
                x = max_x
                y = currPoly[i-1].y + ( currPoly[i].y - currPoly[i-1].y ) * ( x - currPoly[i-1].x ) / ( currPoly[i].x - currPoly[i-1].x )
                result.append(Point(x,y))
            else:
                result.append(currPoly[i])

    currPoly = result
    result = []

    # Down Clipping
    for i in range(len(currPoly)):
        if currPoly[i-1].y > max_y:
            if currPoly[i].y > max_y:
                continue
            else:
                y = max_y
                x = currPoly[i-1].x + ( currPoly[i].x - currPoly[i-1].x ) * ( y - currPoly[i-1].y ) / ( currPoly[i].y - currPoly[i-1].y )
                result.append(Point(x,y))
                result.append(currPoly[i])
        else:
            if currPoly[i].y > max_y:
                y = max_y
                x = currPoly[i-1].x + ( currPoly[i].x - currPoly[i-1].x ) * ( y - currPoly[i-1].y ) / ( currPoly[i].y - currPoly[i-1].y )
                result.append(Point(x,y))
            else:
                result.append(currPoly[i])

    return result

poly = [Point(80,200), Point(250,60), Point(320, 240), Point(250, 380)]

p = Polygon(poly)
p.setWidth(4)
p.setOutline('Green')
p.draw(win)

p = Polygon(polyClip(poly))
p.setWidth(4)
p.setOutline('Red')
p.draw(win)



