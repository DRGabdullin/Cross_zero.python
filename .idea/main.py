from functions import *


def main():
    instructions()
    human, comp = question()
    board = area()
    yes_no = who()
    acquaintance()
    winner = win(board)
    while winner == 0:
        if yes_no == 'y':
            move = player(board, human)
            board[move] = human
            display(board)
            winner = win(board)
            yes_no = 'x'
        else:
            move = computer(board, human, comp)
            board[move] = comp
            display(board)
            winner = win(board)
            yes_no = 'y'
    end(winner, comp, human)

    another()


main()
