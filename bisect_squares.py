# Bisect squares - Problem 16.13
# Assume that the top and bottom of the squares are parallel to the x-axis
# Peter Koppelman January 23, 2018


def bisect(square1, square2):
    def validate(sq):
        if sq[0][0] == sq[1][0] and sq[1][1] == sq[3][1] and \
           sq[3][0] == sq[2][0] and sq[2][1] == sq[0][1]:
            pass
        else:
            exit('One of the objects is not a square. Please check the data')
        if sq[3][0] == sq[0][0] and sq[3][1] == sq[0][1]:
            exit('One of the objects is a point')

    def ctr_point(x_bot_left, x_top_right, y_bot_left, y_top_right):
        return [(x_bot_left + x_top_right)/2, (y_bot_left + y_top_right)/2]

    def calc_slope(x1, y1, x2, y2):
        return (y2 - y1)/(x2 - x1)

    def extend_end_pts(ctr_pt, x_bot_left, slope, sq_no):
        return round(ctr_pt - (ctr_pt - x_bot_left) * 1/slope, 3) if sq_no == '1' else \
            round(ctr_pt + (x_bot_left - ctr_pt) * 1/slope, 3)

    # validate the data. Make sure that the objects are squares.
    validate(square1)
    validate(square2)

    # Calculate the center point of each square
    ctr_pt1 = ctr_point(square1[0][0], square1[3][0], square1[0][1], square1[3][1])
    ctr_pt2 = ctr_point(square2[0][0], square2[3][0], square2[0][1], square2[3][1])
    print('center point 1 is ', ctr_pt1)
    print('center point 2 is ', ctr_pt2)

    # Calculate the slope of the curve using the center points.
    if ctr_pt2[0] == ctr_pt1[0]:  # special case vertical line
        sq1_inside = ctr_pt1[0], square1[0][1]
        sq2_outside = ctr_pt2[0], square2[3][1]
    elif ctr_pt2[1] == ctr_pt1[1]:  # special case horizontal line
        sq1_inside = square1[0][0], ctr_pt1[1]
        sq2_outside = square2[3][0], ctr_pt2[1]
    elif abs(square1[3][0]) <= abs(square2[0][0]) and \
         abs(square1[1][0]) >= abs(square2[2][0]):  # square2 is to the right or left of square1
        slope = calc_slope(ctr_pt1[0], ctr_pt1[1], ctr_pt2[0], ctr_pt2[1])
        sq1_inside = square1[0][0], extend_end_pts(ctr_pt1[0], square1[0][0], slope, '1')
        sq2_outside = square2[3][0], extend_end_pts(ctr_pt2[0], square2[0][0], slope, '2')
    else:  # square2 starts to the left of square1
        slope = calc_slope(ctr_pt1[0], ctr_pt1[1], ctr_pt2[0], ctr_pt2[1])
        sq1_inside = extend_end_pts(ctr_pt1[0], square1[0][1], slope, '1'), square1[0][1]
        sq2_outside = extend_end_pts(ctr_pt2[0], square2[0][1], slope, '2'), square2[3][1]

    print('Point on square 1 for bisect is {}. Point on square 2 for bisect is {}'
          .format(sq1_inside, sq2_outside))


if __name__ == '__main__':
    # points on the square: bottom left, top left, bottom right, top right
    square_1 = [(4, 4), (4, 8), (8, 4), (8, 8)]
    square_2 = [(6, 10), (6, 14), (10, 10), (10, 14)]
    # square_2 = [(6, 4), (6, 8), (10,4), (10, 8)]  # horizontal
    # square_2 = [(4, 12), (4, 16), (8, 12), (8, 16)] # vertical

    bisect(square_1, square_2)
