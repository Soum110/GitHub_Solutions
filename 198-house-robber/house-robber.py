class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        def f(ind):
            if ind == 0:
                return nums[ind]

            if ind < 0:
                return 0

            if dp[ind] != -1:
                return dp[ind]

            pick = nums[ind] + f(ind - 2)
            unpick = 0 +f(ind - 1)

            dp[ind] = max(pick, unpick)
            return dp[ind]

        return f(len(nums) - 1)