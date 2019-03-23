''' Smallest difference - find a pair of values in two different
arrays (lists) that have the smallest non-negative difference.
Problem 16.6 Cracking the Coding Interview
Peter Koppelman Jan 4, 2018
'''


def abs_diff(list_1, list_2):
    list_1 = [float(x) for x in list_1 if type(x) == (int or float)]
    list_2 = [float(x) for x in list_2 if type(x) == (int or float)]

    len_1 = len(list_1)
    len_2 = len(list_2)
    if len_1 == 0 or len_2 == 0:
        exit('Length of one or more of the lists was 0')

    first = max(list_1)
    second = max(list_2)
    smallest_diff = abs(first - second)

    if smallest_diff != 0:
        for x in range(0, len_1):
            for y in range(0, len_2):
                delta = abs(list_1[x] - list_2[y])
                if delta <= smallest_diff:
                    smallest_diff = delta
                    first = list_1[x]
                    second = list_2[y]
                    if smallest_diff == 0:
                        break

    print(smallest_diff, first, second)

    # merge the two lists and get a unique sorted list
    new_list = sorted(list(set(list_1 + list_2)))
    new_len = len(new_list)
    if new_len == 0 or new_len == 1:
        exit('There is not enough data in the list to compare')
    delta = new_list[new_len - 1] - new_list[0]

    for x in range(0, new_len-1):
        new_delta = new_list[x+1] - new_list[x]
        if new_delta < delta:
            delta = new_delta
            first = new_list[x]
            second = new_list[x+1]

    print('Single sorted list')
    print('Delta = ',delta, ' First = ',first, 'Second = ',second)


if __name__ == '__main__':
    # list_a = [1, 3, 15, 11, 2]
    list_a = [1, 3, 15, 102, 18, 99, 65, 195, 765, 459, 67, 9, 33, 82,
              893, 69, 81, 350, 238, 150, 62, 59, 37, 725, 89, 112]
    # list_b = [23, 127, 235, 19, 8]
    list_b = [23, 'c', 235, 19, 8, 167, 389, 100, 435, 97, 88, 14, 27,
              199, 285, 590, 39, 715, 991, 917, 824, 842, 742, 176]
    abs_diff(list_a, list_b)