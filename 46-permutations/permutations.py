class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def f(arr, mp):
            if len(arr) == len(nums):
                res.append(arr[:])
                return

            for i in range(len(nums)):
                if nums[i] in mp and mp[nums[i]] == 1:
                    continue
                arr.append(nums[i])
                mp[nums[i]] = 1
                f(arr, mp)
                arr.pop()
                mp[nums[i]] = 0
        f([], {})
        return res