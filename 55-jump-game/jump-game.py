class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxreach = 0
        last = len(nums)
        for i in range(len(nums)):
            if i > maxreach:
                return False
            maxreach = max(maxreach, i + nums[i])
        return True

## 'i > reach' is trying to know can I jump to the index i using the present reach or not