from typing import List

class Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            for j in range(9):
                
                if board[i][j] != '.':
                    
                    if not self.isValid(board, board[i][j], i, j):
                        return False
        
        return True
    
    
    def isValid(self, board, elem, row, col):
        
        # Check row
        for j in range(9):
            if j != col and board[row][j] == elem:
                return False
        
        # Check column
        for i in range(9):
            if i != row and board[i][col] == elem:
                return False
        
        # Check 3x3 box
        startRow = (row // 3) * 3
        startCol = (col // 3) * 3
        
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                
                if (i != row or j != col) and board[i][j] == elem:
                    return False
        
        return True