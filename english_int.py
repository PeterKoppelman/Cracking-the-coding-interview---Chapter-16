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

    print('number = ', nmbr)
    xnmbr = abs(nmbr)  # absolute value of number
    if xnmbr <= 19:  #Special case
        return special_case(xnmbr)

    # Turn string of numbers into a list and then reverse it so that the
    # largest numbers will be first.
    number_list = []
    for x in range(len(str(xnmbr)), 0, -3):
        if x > 3:
            number_list.append(str(xnmbr)[x - 3: x])
        else:
            number_list.append(str(xnmbr)[0: x])
    # reverse list
    new_list = number_list[::-1]

    print('new list = ', new_list)
    # print('length new list = ', len(new_list))

    # run the for loop looking at each item in the list and creating a word for it.
    name_number = ''
    for x in range(0, len(new_list)):
        working_list = new_list[x]
        if x == 0:  # First loop. May not have 3 digits.
            if len(working_list) == 3:  # 3 digit
                if int(working_list[1:3]) <= 19:
                    name_number = name_number + list_ones[int(str(working_list)[0])] + \
                                  list_other[x] + special_case(int(working_list[1:3]))
                else:
                    name_number = name_number + list_ones[int(str(working_list)[0])] + \
                                  list_other[x] + \
                                  list_tens[int(str(working_list)[1])] + \
                                  list_ones[int(str(working_list)[2])]
            elif len(working_list) == 2:  # 2 digits
                if int(working_list[0:2]) <= 19:
                    name_number = name_number + special_case(int(working_list[0:2]))
                else:
                    name_number = name_number + list_tens[int(str(working_list)[0])] + \
                                  list_ones[int(str(working_list)[1])]
            else:  # 1 digit
                name_number = name_number + list_ones[int(str(working_list)[0])]

            name_number = name_number + list_other[len(new_list) - 1]
        else:
            if int(working_list) <= 19:
                name_number = name_number + special_case(int(working_list))
            elif 19 < int(working_list) <= 99:
                name_number = name_number + list_tens[int(str(working_list))] + \
                            list_ones[int(str(working_list))]
            else:
                name_number = name_number + list_ones[int(str(working_list)[0])] + \
                            list_other[0] + \
                            list_tens[int(str(working_list)[1])] + \
                            list_ones[int(str(working_list)[2])]
            if x != len(new_list) - 1:
                name_number = name_number + list_other[len(new_list) - (x + 1)]

    return name_number


if __name__ == '__main__':
    number = 12326
    name = english_int(number)
    sign = 'negative' if number < 0 else ''
    print('{} {}'.format(sign, name))


