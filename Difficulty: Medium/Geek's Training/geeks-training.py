class Solution:
    def maximumPoints(self, mat):
        #why mx not here
        dp = [[-1] * 4 for _ in range(len(mat))]
        
        def f(day, last):
            mx = 0
            
            if day == 0:
                
                for i in range(0, 3):
                    
                    if i != last:
                        mx = max(mx, mat[0][i])
                        
                return mx
                
            if dp[day][last] != -1:
                return dp[day][last]
                
            for j in range(0,3):
                
                if j != last:
                    
                    points = mat[day][j] + f(day - 1, j)
                    mx = max(mx, points)
                    
            dp[day][last] = mx
            
            return dp[day][last]
            
        return f(len(mat) - 1, 3)