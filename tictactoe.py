""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming, 
          and you make use of relevant object-oriented design principles.
"""
from Board import *
from Movement import *
from CheckWinner import *

class tictactoe(object):

    def __init__(self):
        self.movement = Movement()
        self.check = CheckWinner()
        self.board = Board()

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends

        :return: (str) the letter representing the player who won
        """
        win = False
        winner = None

        while win is not True:
            col = int(input('Enter Column(0-2): '))
            row = int(input('Enter Row(0-2): '))
            if not self.in_bound(row, col):
                print('Out of Bounds Try Again')
                break

            if self.occupied(board.board, row, col):
                break

            player = input('Enter Player: ')
            if not self.if_character(player):
                print('Not Valid Player')
                break

            new_board = self.movement.mark_square(col, row, player, board.board)
            win, winner = self.check.has_winner(new_board)

        return winner 
        pass

    def in_bound(self, row, col):
        if row > 2 or col > 2 or row < 0 or col < 0:
            return False
        else:
            return True
        pass

    def if_character(self, player):
        if player == 'X' or player == 'O':
            return True
        else:
            return False
        pass

    def occupied(self, board, row, col):

        if board[row][col] == 'A':
            return False
        else:
            return True

if __name__ == '__main__':

    board = Board()
    ttt = tictactoe()
    # print(board.mark_square(0,0,'X'))
    # print(board.mark_square(1,0,'X'))
    # print(board.mark_square(2,0,'X'))
    # print(board.mark_square(0,0,'X'))
    # print(board.mark_square(1,1,'X'))
    # print(board.mark_square(2,2,'X'))
    #
    # print(board.row_check('X'))
    # print(board.col_check('X'))
    # print(board.diag_check('X'))
    winner = ttt.play_game()
    print("{} has won!".format(winner))

