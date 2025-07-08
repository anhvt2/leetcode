class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag = 0

    def move(self, row: int, col: int, player: int) -> int:
        # +1 for player 1, -1 for player 2
        mark = 1 if player == 1 else -1

        self.rows[row] += mark
        self.cols[col] += mark

        if row == col:
            self.diag += mark

        if row + col == self.n - 1:
            self.anti_diag += mark

        # Check for winning condition
        if (abs(self.rows[row]) == self.n or
            abs(self.cols[col]) == self.n or
            abs(self.diag) == self.n or
            abs(self.anti_diag) == self.n):
            return player

        return 0
