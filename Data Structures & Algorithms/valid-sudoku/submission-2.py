class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[c][r] ==".":
                    continue
                if board[c][r] in rows[r] or board[c][r] in cols[c] or board[c][r] in square[(r//3,c//3)]:
                    return False
                rows[r].add(board[c][r])
                cols[c].add(board[c][r])
                square[(r//3,c//3)].add(board[c][r])

        return True

        