import matplotlib.pyplot as plt
print('许会杰','2125120073')
def orientation(p, q, r):
    """计算三点之间的方向"""
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return -1

def merge_hulls(left_hull, right_hull):
    """合并两个凸包"""
    # TODO: implement merging logic
    # For simplicity, let's use Graham scan to find the convex hull
    points = left_hull + right_hull
    points = sorted(set(points))
    
    if len(points) <= 1:
        return points
    
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

def convex_hull(points):
    """分治法求凸包"""
    if len(points) <= 1:
        return points
    if len(points) == 2:
        return sorted(points)
    
    points = sorted(points)
    mid = len(points) // 2
    left_hull = convex_hull(points[:mid])
    right_hull = convex_hull(points[mid:])
    
    return merge_hulls(left_hull, right_hull)

# 测试点集合
points = [(0, 0), (1, -4), (-1, -5), (-5, -3), (-3, -1), (-1, -3), (-2, -2), (-1, -1), (-2, -1), (-1, 1)]

# 计算并输出凸包
hull = convex_hull(points)
print("convex hull:")
for point in hull:
    print(point[0], point[1])

# 可视化凸包
hull.append(hull[0]) # To complete the loop for visualization
x, y = zip(*points)
hx, hy = zip(*hull)
plt.figure()
plt.plot(x, y, 'o')
plt.plot(hx, hy, 'r-')
plt.show()
