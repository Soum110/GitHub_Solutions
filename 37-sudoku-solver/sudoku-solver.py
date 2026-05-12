from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        digits = "123456789"
        
        def isValid(r, c, k):
            for i in range(9):
                if board[r][i] == k: return False
                if board[i][c] == k: return False
                # 3x3 box check
                if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == k:
                    return False
            return True

        # Find the empty cell with fewest possible digits (MRV)
        def find_best():
            best_r, best_c = -1, -1
            min_options = 10
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        options = sum(isValid(i, j, d) for d in digits)
                        if options < min_options:
                            min_options = options
                            best_r, best_c = i, j
                            if min_options == 1:   # early exit
                                return best_r, best_c
            return best_r, best_c

        def solve():
            r, c = find_best()
            if r == -1:           # no empty cell → board solved
                return True

            for k in digits:
                if isValid(r, c, k):
                    board[r][c] = k
                    if solve():
                        return True
                    board[r][c] = '.'
            return False

        solve()