# number swapper - problem 16.1 Peter Koppelman Jan 6, 2018


def number_swapper(a, b):
    print('starting point: first = {}, second = {}'.format(first, second))
    # suggested way in Cracking the Coding Interview, Assume a > b
    a = a - b
    b = a + b
    a = b - a
    print('Book solution: a = {}, b = {}'.format(a, b))

    # Python shortcut
    a, b = b, a
    print('Python shortcut: a = {}, b = {}'.format(a, b))

    # bit manipulation using XOR (assuming a != b)
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print('Bit manipulation: a = {}, b = {}'.format(a, b))


if __name__ == '__main__':
    first = 9
    second = 5
    number_swapper(first, second)
