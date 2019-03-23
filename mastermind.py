# mastermind - problem 16.15.
# Peter Koppelman - January 30, 2017

import random


def mastermind(list, mylist):
    def validate_data():
        if not all(x == 'R' or x == 'Y' or x == 'G' or x == 'B' for x in list):
            exit('Master list has a problem')
        if not all(x == 'R' or x == 'Y' or x == 'G' or x == 'B' for x in mylist):
            exit('mylist has a problem')

    def randomlist(list):
        random_list = []
        for i in range(len(list)):
            random_list += random.choice(list)
        return random_list

    def hits():
        hit = 0
        for i in range(len(list)):
            if list[i] == mylist[i]:
                hit += 1
        return hit

    def pseudohits():
        pseudohit = 0
        for i in range(0, len(mylist)):
            if mylist[i] in list and mylist[i] != list[i]:
                pseudohit += 1
        return pseudohit

    def print_info():
        print('List =   ', ('{}, ' * len(list)).format(*list))
        print('My List =', ('{}, ' * len(mylist)).format(*mylist))
        print('hits = {}'.format(number_of_hits))
        print('Pseudo hits = {}'.format(number_of_pseudohits))

    validate_data()
    list = randomlist(list)
    number_of_hits = hits()
    number_of_pseudohits = pseudohits()
    print_info()


if __name__ == '__main__':
    masterlist = ['R', 'Y', 'G', 'B']
    mylist = ['R', 'Y', 'G', 'B']
    mastermind(masterlist, mylist)
