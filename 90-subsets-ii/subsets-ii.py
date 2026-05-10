class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        def subset(ind, arr):
            res.append(arr[:])
            
            for i in range(ind, len(nums)):
                if i > ind and nums[i] == nums[i - 1]:
                    continue
                arr.append(nums[i])
                subset(i + 1, arr)

                arr.pop()

        subset(0, [])
        return res