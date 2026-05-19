class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        def f(mi, ni):
            #grid[m][n]
            #Base conditions
            if mi == 0 and ni == 0:
                return 1
            
            if mi < 0 or ni < 0:
                return 0

            if dp[mi][ni] != -1:
                return dp[mi][ni]

            #Recurssions
            right = f(mi, ni - 1)
            bottom = f(mi - 1, ni)

            dp[mi][ni] = right + bottom
            return dp[mi][ni]

        return f(m - 1, n - 1)