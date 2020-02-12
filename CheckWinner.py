class CheckWinner(object):

    def has_winner(self, board):
        """
        Checks to see if there is a current winner of the game
        """
        if self.col_check('X', board):
            return True, 'X'
        elif self.row_check('X', board):
            return True, 'X'
        elif self.diag_check('X', board):
            return True, 'X'
        elif self.col_check('O', board):
            return True, 'O'
        elif self.row_check('O', board):
            return True, 'O'
        elif self.diag_check('O', board):
            return True, 'O'
        else:
            return False, ''

        pass

    def row_check(self, player, board):
        for x in range(len(board)):
            win = True

            for y in range(len(board)):
                if board[x, y] != player:
                    win = False

            if win:
                return win

        return win

    def col_check(self, player, board):
        for x in range(len(board)):
            win = True

            for y in range(len(board)):
                if board[y][x] != player:
                    win = False
                    continue

            if win:
                return win
        return win

    def diag_check(self, player, board):
        win = True

        for x in range(len(board)):
            if board[x, x] != player:
                win = False
        return win
