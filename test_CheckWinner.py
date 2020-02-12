import unittest
from tictactoe import *

class InBounds(unittest.TestCase):

    tt = tictactoe()

    def test_Out_of_Bound(self):
        """
        Check when both characters are out of bounds
        :return: Return false because it is out of bounds
        """
        self.assertEqual(self.tt.in_bound(3, 3), False)

    def test_in_Bound(self):
        """
        Tests when both row and col are in bounds
        :return: True because they are in bound
        """
        self.assertEqual(self.tt.in_bound(2, 2), True)

    def test_Out_of_Bound2(self):
        """
        Tests if one is out of bounds and one is in bounds
        :return: False because on is out of bounds
        """
        self.assertEqual(self.tt.in_bound(3, 12), False)

    def test_Out_of_Bound3(self):
        """
        Tests if one is is a negative number
        :return: False because it is negative
        """
        self.assertEqual(self.tt.in_bound(-3, 1), False)


if __name__ == '__main__':
    unittest.main()
