# A method that finds the maximum of two numbers. Problem 16.7
# Peter Koppelman January 12, 2018

# import numpy as np


def number_max(first, second):

    def flip(bit):
        return 1 ^ bit

    def sign(value):
        return flip((value >> 31) & 0x1)

    def get_max(a, b):
        c = a - b
        print('Underlying Values')
        print('a = {}'.format(a))
        print('b = {}'.format(b))
        print('c = {}'.format(c))
        print()
        print('Sign')
        sa = sign(a)
        print('sa = {}'.format(sa))
        sb = sign(b)
        print('sb = {}'.format(sb))
        sc = sign(c)
        print('sc = {}'.format(sc))
        print()

        sign_of_a = sa ^ sb
        print('sign of a = {}'.format(sign_of_a))
        sign_of_c = flip(sa ^ sb)
        print('sign of c = {}'.format(sign_of_c))

        k = (sign_of_a * sa) + (sign_of_c * sc)
        print('k =  {}'.format(k))
        q = flip(k)
        print('q = {}'.format(q))
        return a * k + b * q

    x = get_max(first, second)
    # print('Max number is {}'.format(get_max(first, second)))
    return x


if __name__ == '__main__':
    x = -8
    y = 3
    max_number = number_max(x, y)
    print('Max number = {}'.format(max_number))
