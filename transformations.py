from graphics import *
import time

win = GraphWin('Transformations', 600, 600)

l = Line(Point(200,300), Point(400, 300))
l.draw(win)

for i in range(50):
    l.p1.y += 1
    time.sleep(0.1)
    l.undraw()
    l.draw(win)

