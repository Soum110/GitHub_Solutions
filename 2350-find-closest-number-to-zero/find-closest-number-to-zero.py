class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minimum = nums[0]
        for i in range(len(nums)):
            if abs(nums[i]) < abs(minimum):
                minimum = nums[i]
            elif abs(nums[i]) == abs(minimum) and nums[i] > minimum:
                minimum = nums[i]
        return minimum
            
        