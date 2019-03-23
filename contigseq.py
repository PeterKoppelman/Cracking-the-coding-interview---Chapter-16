# Contiguous Sequence - problem 16.17
# Peter Koppelman - Feb 1, 2018


def contigseq(list):
    def calc_combos():
        no_of_combos = 0
        for i in range(len(list) + 1):
            no_of_combos += i
        return no_of_combos

    def calc_list():
        list_sum = sum(list)
        list_elements = list
        upper = len(list)
        for i in range(combos):
            for j in range(upper):
                new_sum = sum(list[j:upper])
                new_list = list[j:upper]
                if new_sum > list_sum:
                    list_sum = new_sum
                    list_elements = new_list
            upper -= 1
            if upper == 0:
                break
        return list_sum, list_elements

    def print_info():
        print('List = ', list)
        print('number of combinations = ', combos)
        print()
        print('Final value = ', list_sum)
        print('Final string = ', list_elements)

    combos = calc_combos()
    list_sum, list_elements = calc_list()
    print_info()


if __name__ == '__main__':
    list = [-8, 3, -2, 4, -10]
    contigseq(list)
