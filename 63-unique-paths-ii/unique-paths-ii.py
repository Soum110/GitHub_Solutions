class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1] * n for _ in range(m)]

        def f(mi, ni, ogrid):

            #Boundary Conditions
            if mi < 0 or ni < 0:
                return 0

            if ogrid[mi][ni] == 1:
                return 0

            if mi == 0 and ni == 0:
                return 1

            if dp[mi][ni] != -1:
                return dp[mi][ni]
            
            #Recurssion
            up = f(mi - 1, ni, ogrid)
            left = f(mi, ni - 1, ogrid)

            dp[mi][ni] = up + left
            return dp[mi][ni]
        return f(m - 1, n - 1, obstacleGrid)