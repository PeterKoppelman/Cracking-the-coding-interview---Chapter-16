# diving_board - write a method to generate the number of possible combinations of wood
# planks to build a diving board - problem 16.11.
#
# Peter Koppelman January 20, 2018


def diving_board(short, long, number):
    def data_validation(short, long, number):
        # Check to see if all values are >= 0
        if short < 0 or long < 0 or number < 0:
            exit('At least one of the values is less than 0. All of them must be greater than or equal to 0')

        # Check to see if all values are integers
        if (type(short) or type(long) or type(number)) is not int:
            exit('At least one of the values is not an integer. All of them must be integers')

    def create_list(short, long, number):
        # Create tuples in a list. Each tuple will have the number of shorter boards, longer boards
        # and the length of the diving board
        combination = []
        for x in range(0, number + 1):
            y = x, number - x, (short * x) + (long * (number - x))
            combination.append(y)
        return combination

    def print_data(combination):
        print('Shorter Longer  Length')
        for x in combination:
            print('{:^7} {:^6} {:^8}'.format(x[0], x[1], x[2]))

    # Start main program. Call the functions...
    data_validation(short, long, number)
    # combination = create_list(short, long, number)
    # print_data(combination)
    print_data(create_list(short, long, number))


if __name__ == '__main__':
    shorter = 12
    longer = 24
    number_boards = 7
    diving_board(shorter, longer, number_boards)
