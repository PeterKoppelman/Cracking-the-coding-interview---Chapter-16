# subsort - problem 16.16
# Peter Koppelman January 31, 2018


def subsort(orig_list):
    new_list = sorted(orig_list)
    print(orig_list)
    print(new_list)

    lower = 0
    higher = 0

    for i in range(0, len(orig_list)):
        if orig_list[i] != new_list[i]:
            lower = i
            lower_value = new_list[i]
            for j in range(0, len(orig_list)):
                if orig_list[j] == lower_value:
                    higher = j + 1
                    break
            break

    print('Lower value = ', lower)
    print('Higher value = ', higher)

if __name__ == '__main__':
    list = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    subsort(list)

