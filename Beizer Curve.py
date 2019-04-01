from graphics import *
max_x = 600; max_y = 600;
win = GraphWin('Beizer', max_x, max_y)

def mat_mul(x, y):
    dim_x = (len(x), len(x[0]))
    dim_y = (len(y), len(y[0]))
    if (dim_x[1] != dim_y[0]):
        return False
    result = []

    for i in range(dim_x[0]):
        tmp_mat = []
        for j in range(dim_y[1]):
            tmp = 0
            for k in range(dim_x[1]):
                tmp += x[i][k] * y[k][j]
            tmp_mat.append(tmp)
        result.append(tmp_mat)

    return result;

def beizer_draw(p1, p2, p3, p4):
    M = [[-1,3,-3,1], [3,-6,3,0],[-3,3,0,0],[1,0,0,0]]
    P_x = [[p1.x], [p2.x], [p3.x], [p4.x]]
    P_y = [[p1.y], [p2.y], [p3.y], [p4.y]]
    MP_x = mat_mul(M, P_x)
    MP_y = mat_mul(M, P_y)

    steps = 1000
    for t in range(steps):
        t1 = t / steps
        T = [[t1**3, t1**2, t1, 1]]
        x = mat_mul(T, MP_x)
        y = mat_mul(T, MP_y)
        Point(x[0][0],y[0][0]).draw(win)

'''p1 = Point(150, 500)
p2 = Point(170, 200)
p3 = Point(220, 220)
p4 = Point(350, 400)

beizer_draw(p1,p2,p3,p4)
beizer_draw(p1,Point(500,100),p3,p4)
beizer_draw(Point(250,400),p2,p3,p4)'''

beizer_draw(Point(300,300), Point(100,50), Point(500,50), Point(300,300))
beizer_draw(Point(300,300), Point(100,50), Point(500,50), Point(300,300))



                
