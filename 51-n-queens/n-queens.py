class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #Creating the 2D array [[....][....]..[....]]
        arr = [['.' for _ in range(n)] for _ in range(n)]
        #Result 
        res = []
        #Recursive function to check for validity of each column for placing the 'Q'
        def f(col, arr):
            #Boundary condition
            if col == n:    #When column value exceeds the len(col) append the present array to result array by coping 
                res.append([''.join(r) for r in arr])
                return
            #Recursive calling
            for row in range(n):    #Iterate through each row of each column and check validity to place 'Q'
                if (isSafe(col, row, arr)):
                    arr[row][col] = 'Q'
                    f(col + 1, arr)
                    arr[row][col] = '.'
        def isSafe(col, row, arr):  #Implementing the validity checker 

            #Checks for upper diagonal for any other 'Q'
            tcol = col
            trow = row
            while (tcol >= 0 and trow >= 0):
                if arr[trow][tcol] == 'Q':
                    return False
                trow -= 1
                tcol -= 1
            
            #Checks for the present row for any other 'Q'
            trow = row
            tcol = col
            while tcol >= 0:
                if arr[trow][tcol] == 'Q':
                    return False
                tcol -= 1
            
            #Checks for lower diagonal for any other 'Q'
            trow = row
            tcol = col
            while (tcol >= 0 and trow < n):
                if arr[trow][tcol] == 'Q':
                    return False
                tcol -= 1
                trow += 1
            
            #If not found return True
            return True
        
        f(0, arr)
        return res

