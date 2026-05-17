class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        def f(num):
            if num == 0:
                return 1
            if num == 1:
                return 1
            if dp[num] != -1:
                return dp[num]
            dp[num] = f(num - 1) + f(num - 2)
            return dp[num]
        return f(n)
        