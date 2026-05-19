class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        wolast = nums[:-1]
        wofirst = nums[1:]
        def f(arr):

            dp = [-1] * len(arr)

            def solve(ind):
                if ind == 0:
                    return arr[ind]

                if ind < 0:
                    return 0

                if dp[ind] != -1:
                    return dp[ind]

                pick = arr[ind] + solve(ind - 2)
                unpick = 0 + solve(ind - 1)

                dp[ind] = max(pick, unpick)
                return dp[ind]

            return solve(len(arr) - 1)

        return max(f(wolast), f(wofirst))