from Board import *

class Movement(object):


    def mark_square(self, column, row, player, board):
        """
        Marks a square at coordinate (column, row) for player

        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (str) the X or O representation of which player to mark in square

        :return: ????
        """
        board[row][column] = player
        return board

        pass