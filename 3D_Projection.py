from graphics import *

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

    return result

win = GraphWin('3D', 1200, 1200)
# Distance of screen from Camera
d = 10

class Point_3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_2d(self, d):
        p = [[self.x], [self.y], [self.z], [1]]
        p = mat_mul([[1,0,0,0], [0,1,0,0],[0,0,0,0],[0,0,1/d,1]], p)
        return Point(600 + p[0][0] / (1+self.z/d), 600 - p[1][0] / (1+self.z/d))

class Cuboid:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self):
        for i in (self.p1.x, self.p2.x):
            for j in (self.p1.y, self.p2.y):
                for k in (self.p1.z, self.p2.z):
                    Line(Point_3d(i, j, self.p1.z).get_2d(d), Point_3d(i, j, self.p2.z).get_2d(d)).draw(win)
                    Line(Point_3d(i, self.p1.y, k).get_2d(d), Point_3d(i, self.p2.y, k).get_2d(d)).draw(win)
                    Line(Point_3d(self.p1.x, j, k).get_2d(d), Point_3d(self.p2.x, j, k).get_2d(d)).draw(win)

class Tetrahedron:
    def __init__(self, p1,p2,p3,p4):
        self.points = [p1, p2, p3, p4]

    def draw(self):
        for p1 in self.points:
            for p2 in self.points:
                Line(Point_3d(p1.x, p1.y, p1.z).get_2d(d), Point_3d(p2.x, p2.y, p2.z).get_2d(d)).draw(win)

Cuboid(Point_3d(100, 100, 2), Point_3d(400, 400, 10)).draw()
Cuboid(Point_3d(-100, -200, 2), Point_3d(-400, 400, 12)).draw()

p1 = Point_3d(100, -100, 0)
p2 = Point_3d(400, -100, 0)
p3 = Point_3d(250, -250, 0)
p4 = Point_3d(250, -50, 4)

Tetrahedron(p1, p2, p3, p4).draw()
