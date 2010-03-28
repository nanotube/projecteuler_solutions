import math
data = open('102 - triangles.txt').readlines()

def intersects(a, b, axis):
    axis = [1,0][axis]
    if (a[axis] > 0 and b[axis] < 0) or (a[axis] < 0 and b[axis] > 0):
        try:
            m = (a[1] - b[1])/(a[0] - b[0])
            b = a[1] - m*a[0]
            if axis == 1:
                try:
                    intercept = -b/m
                except:
                    intercept = None
            if axis == 0:
                intercept = b
        except ZeroDivisionError: # on the m
            if axis == 1:
                intercept = None
            if axis == 0:
                intercept == a[0]
        return intercept
    else:
        return None

goodones = 0
for line in data:
    intercepts = [[],[]]
    points = [float(i.strip()) for i in line.split(',')]
    a = points[:2]
    b = points[2:4]
    c = points[4:]
    for i in [(a, b, 0), (a, b, 1), (b, c, 0), (b, c, 1), (a, c, 0), (a, c, 1)]:
        intercept = intersects(*i)
        if intercept is not None:
            intercepts[i[2]].append(intercept)
    if len(intercepts[0]) == 2:
        if (intercepts[0][0] > 0 and intercepts[0][1] < 0) or (intercepts[0][0] < 0 and intercepts[0][1] > 0):
            goodones += 1
    elif len(intercepts[1]) == 2:
        if (intercepts[1][0] > 0 and intercepts[1][1] < 0) or (intercepts[1][0] < 0 and intercepts[1][1] > 0):
            goodones += 1

print goodones #228