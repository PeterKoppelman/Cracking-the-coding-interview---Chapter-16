''' Create an algorithm to determine if someone has won a game of
tic tac toe. Peter Koppelman Jan 4, 2018

There are nine boxes on a tic tac toe board. They will be numbered:
1 2 3
4 5 6
7 8 9

In case there are 16 boxes (4 x 4) on the board...
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16

There are (2x + 2) winning combinations
'''
import math


def tictactoe():
    # Box number - n = null, w = white and b = black
    board = {1: 'b', 2: 'w', 3: 'w', 4: 'b', 5: 'n', 6: 'n',
             7: 'b', 8: 'n', 9: 'n'}

    if len(board) % math.sqrt(len(board)) != 0:
        exit('the board must by n x n, it is not')

    board_size = int(math.sqrt(len(board)))
    no_combos = int((board_size * 2) + 2)
    len_board = len(board)

    print('board size {} by {}'.format(board_size, board_size))
    print('combos {}'.format(no_combos))
    print('len board {}'.format(len_board))
    print()

    combo = []

    def horizontal():
        starting_pt = 1
        ending_pt = board_size + 1
        for hcnt in range(0, board_size):
            cnt = 0
            temp = []
            for horiz in range(starting_pt, ending_pt):
                cnt += 1
                temp.append(horiz)
                if cnt == board_size:
                    combo.append(temp)
                    if ending_pt < len_board:
                        starting_pt = ending_pt
                        ending_pt = starting_pt + board_size

    def vertical():
        cnt = 1
        starting_pt = 1
        ending_pt = len_board - (board_size - 1)
        for vcnt in range(1, board_size):
            temp = []
            for vert in range(starting_pt, ending_pt):
                temp.append(cnt)
                cnt += board_size
                if cnt == ending_pt:
                    temp.append(cnt)
                    combo.append(temp)
                    temp = []
                    if ending_pt < len_board:
                        starting_pt += 1
                        ending_pt += 1
                        cnt = starting_pt

    def diagonal():
        # outside diagonal
        cnt = 1
        starting_pt = 1
        ending_pt = len_board
        temp = []
        for o_diag in range(starting_pt, ending_pt):
            temp.append(cnt)
            cnt += board_size + 1
            if cnt == ending_pt:
                temp.append(cnt)
                combo.append(temp)
                break

        # inside diagonal
        cnt = board_size
        starting_pt = 1
        ending_pt = len_board - (board_size - 1)
        temp = []
        for i_diag in range(starting_pt, ending_pt):
            temp.append(cnt)
            cnt += board_size - 1
            if cnt == ending_pt:
                temp.append(cnt)
                combo.append(temp)
                break

    def check_board():
        board_values = list(board.values())
        null = 0
        white = []
        black = []
        for icnt in range(0, len_board):
            if board_values[icnt] == 'n':
                null += 1
            elif board_values[icnt] == 'w':
                white.append(icnt+1)
            else:
                black.append(icnt+1)
        return null, white, black

    def check_for_winner(null, white, black):
        if null == len_board:
            print('no moves yet')
            exit()

        for x in range(0, len(board) -1):
            if len(white) >= board_size and \
                            set(white) & (set(combo[x])):
                print('white has won')
                exit()
        for x in range(0, len(board) - 1):
            if len(black) >= board_size and \
                            set(black) & (set(combo[x])):
                print('black has won')
                exit()

        # no winner yet...
        print('no one has won yet, make another move or start another game')

    horizontal()
    vertical()
    diagonal()

    print('Possible winning combinations')
    for x in combo:
        print(*x)
        if int(combo.index(x) + 1) % board_size == 0:
            print()
    print()

    null, white, black = check_board()
    check_for_winner(null, white, black)


if __name__ == '__main__':
    tictactoe()
