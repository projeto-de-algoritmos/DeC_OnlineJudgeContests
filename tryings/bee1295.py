def dist(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2) ** 0.5

def closest_pair(points):
    length = len(points)
    if length == 2: return dist(points[0], points[1])
    if length == 3: return min(dist(points[0], points[1]), dist(points[1], points[2]), dist(points[0], points[2]))

    mid = points[length//2]
    midIndex = points.index(mid)
    dl = closest_pair(points[:midIndex])
    dr = closest_pair(points[midIndex:])
    d = min(dl, dr)

    pointsInRange = sorted([point for point in points if (point[0] >= mid[0] - d) and (point[0] <= mid[0] + d)], key=lambda x: x[0])
    for i in range(len(pointsInRange)):
        for j in range(7):
            if i + j < len(pointsInRange) and pointsInRange[i] != pointsInRange[i + j]:
                d = min(d, dist(pointsInRange[i], pointsInRange[i + j]))

    return d


N = int(input())

while N:
    points = []
    for _ in range(N):
        x, y = map(float, input().split())
        points.append((x, y))
    points.sort(key=lambda x: x[0])
    if N == 1: print("INFINITY")
    else:
        minDist = closest_pair(points)
        print("INFINITY" if minDist > 10000 else "%1.4f" %minDist)
    N = int(input())