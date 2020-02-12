import unittest
from tictactoe import *
import numpy as np

class test_occupied(unittest.TestCase):

    tt = tictactoe()

    def test_occupied1(self):
        """
        Tests if this available slot is occuiped
        :return: Should return False because it is avalaiable
        """
        array = np.array(['A'])
        self.assertFalse(self.tt.occupied(array, 0, 0))

    def test_occupied2(self):
        """
        Tests if this available slot is occupied
        :return: Should return True because it is occupied by a player
        """
        array = np.array(['O'])
        self.assertTrue(self.tt.occupied(array, 0, 0))


if __name__ == '__main__':
    unittest.main()
