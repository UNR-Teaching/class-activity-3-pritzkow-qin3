import unittest
from tictactoe import *


class ifCharacter(unittest.TestCase):

    tt = tictactoe()

    def test_not_chara(self):
        """
        Tests a character that should not be entered
        :return: Should return false because it is not a valid player
        """
        self.assertEqual(self.tt.if_character('Y'), False)

    def test_is_chara(self):
        """
        Tests a character that is correct
        :return: Should return true because it is a valid player
        """
        self.assertEqual(self.tt.if_character('X'), True)

    def test_isnot_chara(self):
        """
        Tests a string that should not be entered
        :return: Should return false because it is not a valid player/string
        :return:
        """
        self.assertEqual(self.tt.if_character('NOT'), False)

    def test_isnot_int(self):
        """
        Tests if a integer is entered
        :return: Should return false because it not a valid player / int
        """
        self.assertEqual(self.tt.if_character(1), False)


if __name__ == '__main__':
    unittest.main()
