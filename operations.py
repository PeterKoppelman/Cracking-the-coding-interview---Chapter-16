# Operations - Write methods to multiply, add and subtract only using the add operator.
# Problem 16.9 - Peter Koppelman


def operations(a, b):
    def negate(num):
        neg = 0
        new_sign = 1 if num < 0 else -1
        while num != 0:
            neg += new_sign
            num += new_sign
        return neg

    def multiply(a, b):
        c = 0
        for x in range(0, abs(b)):
            c += a
        return c if b >= 0 else -c

    def subtract(a, b):
        return a + negate(b)

    def divide(a, b):
        return 'N/A' if a == 0 or b == 0 else multiply(1/a, b)

    mult = multiply(a, b)
    sub = subtract(a, b)
    div = divide(a, b)
    return mult, sub, div


if __name__ == '__main__':
    test_set = [(4, 8), (8, 4), (-4, -8), (-8, -4), (4, -8), (-4, 8), (0, 0), (0, 4)]
    for x in range(0, len(test_set)):
        print('A = {}, B = {}'.format(test_set[x][0], test_set[x][1]))
        result = operations(test_set[x][0], test_set[x][1])
        print('Multiplication result is {}, Subtraction result is {}, Division result is {}'
              .format(result[0], result[1], result[2]))
        print()
