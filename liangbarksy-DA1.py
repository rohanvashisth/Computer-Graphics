from graphics import *
win = GraphWin('Clipping', 600, 600)

min_x = 150
max_x = 450
min_y = 150
max_y = 450

def clip_test(p, q):
    global u_min
    global u_max
    if(p < 0):
        # Entry Point
        u = q / p
        if (u > u_max):
            return False
        elif (u > u_min):
            u_min = u
    elif (p > 0):
        # exit point
        u = q / p
        if ( u < u_min):
            return false
        elif (u < u_max):
            u_max = u

        elif (q < 0):
            return False
            # Parellel and outside

    return True
        

def liang_barsky_clip(p1, p2):
    global u_min
    global u_max
    u_min, u_max = 0, 1
    (x1, y1) = (p1.x, p1.y)
    (x2, y2) = (p2.x, p2.y)

    if (clip_test(x1 - x2, x1 - min_x)):
        if (clip_test(x2 - x1, max_x - x1)):
            if (clip_test(y1 - y2, y1 - min_y)):
                if (clip_test(y2 - y1, max_y - y1)):
                    print(u_min, u_max)
                    p2.x = p1.x + u_max * (x2-x1)
                    p2.y = p1.y + u_max * (y2-y1)
                    p1.x += u_min * (x2-x1)
                    p1.y += u_min * (y2-y1)
                    print(p1,p2)
                    return True

    return False


# Graphing of points
AcceptanceRegion = Rectangle(Point(min_x, min_y), Point(max_x, max_y))
AcceptanceRegion.setFill('green')
AcceptanceRegion.draw(win)

def clip_and_show(p1, p2):
    l = Line(p1,p2)
    l.setOutline('green')
    l.setWidth(4)
    l.draw(win)

    if (liang_barsky_clip(p1,p2)):
        l = Line(p1,p2)
        l.setOutline('red')
        l.setWidth(4)
        l.draw(win)

clip_and_show(Point(40, 200), Point(500,300))
clip_and_show(Point(200,300), Point(400,200))
clip_and_show(Point(80,250), Point(110,500))
