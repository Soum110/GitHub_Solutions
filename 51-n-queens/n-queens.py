class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        arr = [['.' for _ in range(n)] for _ in range(n)]
        res = []
        def f(col, arr):
            if col == n:
                res.append([''.join(r) for r in arr])
                return
            
            for row in range(n):
                if (isSafe(col, row, arr)):
                    arr[row][col] = 'Q'
                    f(col + 1, arr)
                    arr[row][col] = '.'
        def isSafe(col, row, arr):
            tcol = col
            trow = row
            while (tcol >= 0 and trow >= 0):
                if arr[trow][tcol] == 'Q':
                    return False
                trow -= 1
                tcol -= 1
            
            trow = row
            tcol = col
            while tcol >= 0:
                if arr[trow][tcol] == 'Q':
                    return False
                tcol -= 1
            
            trow = row
            tcol = col
            while (tcol >= 0 and trow < n):
                if arr[trow][tcol] == 'Q':
                    return False
                tcol -= 1
                trow += 1
            return True
        f(0, arr)
        return res

