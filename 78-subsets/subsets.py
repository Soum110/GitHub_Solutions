class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def subset(ind, arr):
            if ind >= len(nums):
                res.append(arr[:])
                return
            
            arr.append(nums[ind])
            subset(ind + 1, arr)

            arr.pop()
            subset(ind + 1, arr)
        
        subset(0, [])
        return res