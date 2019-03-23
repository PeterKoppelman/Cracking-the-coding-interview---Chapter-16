# point_of_intersection - problem 16.3
# Peter Koppelman January 7, 2018

import matplotlib.pyplot as plt


def point_of_intersection(x1, y1, x2, y2):

    def slope(x, y):
        return (y[1] - x[1]) / (y[0] - x[0])

    def intercept(start, slope):
        return start[1] - slope * start[0]

    def intercept_pt(sl1, int_1, sl2, int_2):
        x = (int_2 - int_1) / (sl1 - sl2)
        y = sl1 * x + int_1
        return x, y

    def online(a,b,c):
        if c[0] <= max(a[0], b[0]) and c[0] >= min(a[0], b[0]) and \
           c[1] <= max(a[1], b[1]) and c[1] >= min(a[1], b[1]):
            return True

        return False

    def orientation(a, b, c):  # a and b are the endpoints of the line segment.
        value = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
        if value == 0:
            return 0
        elif value >= 0:
            return 1
        else:
            return 2

    def intersect(x1, y1, x2, y2):
        o1 = orientation(x1, y1, x2)
        o2 = orientation(x1, y1, y2)
        o3 = orientation(x2, y2, x1)
        o4 = orientation(x2, y2, y1)

        if o1 != o2 and o3 != o4:
            return True

        # Co-linear tests
        if o1 == 0 and online(x1, x2, y1):
            print('online = ', online)
            return True
        if o2 == 0 and online(x1, y2, y1):
            print('online = ', online)
            return True
        if o3 == 0 and online(x2, x1, y2):
            print('online = ', online)
            return True
        if o4 == 0 and online(x2, y1, y2):
            print('online = ', online)
            return True

        return False

    def graph(x1, y1, x2, y2, intercept_x, intercept_y):
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')
        plt.title('Two Lines')
        plt.plot([x1[0], y1[0]], [x1[1], y1[1]], [x2[0], y2[0]], [x2[1], y2[1]])
        plt.axis([0, 12, 0, 12])
        plt.annotate('Pt of intersection is \n {:.4f}, {:.4f}'.format(intercept_x, intercept_y),
                     xy=(intercept_x, intercept_y), xytext=(intercept_x + 2, intercept_y + 2),
                     arrowprops=dict(facecolor='black', shrink=0.05),)
        plt.show()

    # Print co-ordinates
    print('X1 start {}, {}'.format(x1[0], x1[1]))
    print('X1 end   {}, {}'.format(y1[0], y1[1]))
    print('X2 start {}, {}'.format(x2[0], x2[1]))
    print('X2 end   {}, {}'.format(y2[0], y2[1]))
    print()

    # Calculate slope
    slope1 = slope(x1, y1)
    print('slope of line 1 = {}'.format(slope1))
    slope2 = slope(x2, y2)
    print('slope of line 2 = {}'.format(slope2))
    print()

    # if slopes are the same lines are parallel
    if slope1 == slope2:
        print('Lines are parallel, they will never meet')
        exit()

    # Find points where lines intercept y axis
    intercept_line1 = intercept(x1, slope1)
    intercept_line2 = intercept(x2, slope2)

    # Calculate point of intercept of the lines
    x_intercept, y_intercept = intercept_pt(slope1, intercept_line1, slope2, intercept_line2)
    print('X Intercept is {}'.format(x_intercept))
    print('Y Intercept is {}'.format(y_intercept))
    print()

    x = intersect(x1, x2, y1, y2)
    if x is False:
        print('The line segments intersect')
    else:
        print('The line segments do not intersect')

    graph(x1, y1, x2, y2, x_intercept, y_intercept)


if __name__ == '__main__':
    X1 = (2, 1)
    Y1 = (6, 10)
    X2 = (1, 11)
    Y2 = (8, 6)
    if X1 == Y1 or X2 == Y2:
        print("One or both of the 'lines' is a single point. Please change it/them.")
    elif X1 == X2 and Y1 == Y2:
        print('The two lines are the same. Please change one of them.')
    else:
        point_of_intersection(X1, Y1, X2, Y2)
