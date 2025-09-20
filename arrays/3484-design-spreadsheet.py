from typing import List

class Spreadsheet:
    # 26 columns: 'A'..'Z', rows are 1-indexed in input
    def __init__(self, rows: int):
        self.R = rows
        self.C = 26
        self.grid = [[0] * self.C for _ in range(self.R)]

    # "A1", "B10", ...
    def setCell(self, cell: str, value: int) -> None:
        r, c = self._parse_cell(cell)
        self.grid[r][c] = value

    def resetCell(self, cell: str) -> None:
        r, c = self._parse_cell(cell)
        self.grid[r][c] = 0

    # formula like "=X+Y", where X/Y are either cell refs or non-negative integers
    def getValue(self, formula: str) -> int:
        a, b = formula[1:].split('+', 1)
        return self._token_value(a) + self._token_value(b)

    # ---------- helpers ----------
    def _parse_cell(self, s: str) -> (int, int):
        # s[0] is 'A'..'Z'; the rest is the 1-based row
        c = ord(s[0]) - ord('A')
        r = int(s[1:]) - 1
        return r, c

    def _token_value(self, tok: str) -> int:
        # if token starts with a letter, treat as cell; else parse int
        if tok and 'A' <= tok[0] <= 'Z':
            r, c = self._parse_cell(tok)
            return self.grid[r][c]
        return int(tok)
