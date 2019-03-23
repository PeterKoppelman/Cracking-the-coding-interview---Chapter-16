# palindrome
# Peter Koppelman January 16, 2018


def palindrome(sequence):
    orig_list = []
    for x in range(0, len(sequence)):
        orig_list.append(sequence[x].lower())
    new_list = orig_list[::-1]
    return 'a palindrome' if orig_list == new_list else 'not a palindrome'


if __name__ == '__main__':
    sequence = 'Hannah'
    print('The sequence is {}'.format(palindrome(sequence)))
