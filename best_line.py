# best line. Find a line which passes through the most number of points on a 2 dimensional graph.
# Peter Koppelman January 28, 2018

import matplotlib.pyplot as plt
from statistics import mean
import numpy as np


def best_fit_slope(x, y):
    def slope():
        return ((mean(x)*mean(y)) - mean(x*y)) / ((mean(x)*mean(x)) - mean(x*x))

    def y_intercept():
        return mean(y) - slope * mean(x)

    def graph():
        plt.scatter(x, y)
        y_plot_pts = [y_intercept + slope * i for i in x]
        plt.plot(xs, y_plot_pts)
        plt.grid()
        start_pt = np.array((x[2], y[2]))
        plt.title('Regression Analysis to find Best Fit', fontsize=16)
        trans_angle = plt.gca().transData.transform_angles(np.array((45,)), start_pt.reshape((1, 2)))[0]
        th1 = plt.text(x[1], y[1], 'y = {:.2f} + {}x'.format(y_intercept, slope), fontsize=14,
                       rotation=trans_angle, rotation_mode='anchor')
        plt.show()

    slope = slope()
    y_intercept = y_intercept()
    graph()


if __name__ == '__main__':
    # sample points
    xs = np.array([0, 5, 10, 15, 20])
    ys = np.array([0, 7, 10, 13, 20])

    best_fit_slope(xs, ys)
