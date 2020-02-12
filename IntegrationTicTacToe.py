import unittest
from tictactoe import *
from Board import *
from Movement import *
from CheckWinner import *
import numpy as np

class test_occupied(unittest.TestCase):

    tt = tictactoe()
    board = Board()
    move = Movement()
    check = CheckWinner()

    def test_TicTacToe(self):
        """
        Runs Through the tictactoe class to test it changing board elements
        :return:
        """
        self.oldBoard = np.array([['A', 'A', 'A'], ['A', 'A', 'A'], ['A', 'A', 'A']])
        self.newBoard = np.array([['X', 'A', 'A'], ['A', 'A', 'A'], ['A', 'A', 'A']])
        self.assertTrue(self.tt.in_bound(0, 0))
        self.assertFalse(self.tt.occupied(self.board.board, 0, 0))
        #self.assertEqual(self.move.mark_square(0,0,'X',self.oldBoard), self.newBoard)

if __name__ == '__main__':
    unittest.main()
