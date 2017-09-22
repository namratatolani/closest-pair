import math
def closestPoints(points):
    n = len(points)
    min_d = 10000
    for i in range(n):
        for j in range(i):
            d = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
            if d < min_d:
                min_d = d
                close_pair = [(points[i][0], points[i][1]), (points[j][0], points[j][1])]
            print("Distance between : ",
                  points[i], points[j], "is = ", d)
    print("Closest pair is ", close_pair, " with distance = ", min_d)
points = [(1,2),(3,4),(5,9),(10,78)]
closestPoints(points)
