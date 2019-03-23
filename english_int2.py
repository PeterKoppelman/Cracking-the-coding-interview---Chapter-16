# English int - print an English phrase that describes an integer - problem 16.8
# Peter Koppelman - January 13,2018

list_ones = ['zero ', 'one', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine ',
             'ten ', 'eleven ', 'twelve ', 'thirteen ', 'fourteen ', 'fifteen ', 'sixteen ',
             'seventeen ', 'eighteen ', 'nineteen ']
list_tens = [' ', ' ', 'twenty ', 'thirty ', 'forty ', 'fifty ', 'sixty ', 'seventy ', 'eighty ', 'ninety ']
list_other = ['hundred ', ' thousand ', ' million ', ' billion ']


def english_int(nmbr):

    def special_case(number):
        return list_ones[number]

    def create_list(xnmbr):
        number_list = [str(xnmbr)[x - 3: x] if x > 3 else str(xnmbr)[0: x] for
                       x in range(len(str(xnmbr)), 0, -3)]
        # reverse list
        return number_list[::-1]

    def name_integer(eng_name, working_list, max_loops, cnt):
        if int(working_list) <= 19:
            eng_name += special_case(int(working_list))
        elif 19 < int(working_list) <= 99:
            eng_name += list_tens[int(working_list[0])] + list_ones[int(working_list[1])]
        else:
            eng_name += list_ones[int(working_list[0])] + list_other[0]
            if int(str(working_list[1:3])) <= 19:
                eng_name += special_case(int(working_list[1:3]))
            else:
                eng_name += list_tens[int(working_list[1])] + list_ones[int(working_list[2])]
        return eng_name if cnt + 1 == max_loops else eng_name + list_other[max_loops - (cnt + 1)]

    # Start of program
    print('number = ', nmbr)

    # Turn string of numbers into a list and then reverse it so that the
    # largest numbers will be first.
    new_list = create_list(abs(nmbr))
    print('new list = ', new_list)

    # run the for loop looking at each item in the list and create a word for it.
    name_number = ''
    for x in range(0, len(new_list)):
        name_number = name_integer(name_number, new_list[x], len(new_list), x)
    return name_number


if __name__ == '__main__':
    number = -6479
    name = english_int(number)
    sign = 'negative' if number < 0 else ''
    print('{} {}'.format(sign, name))
