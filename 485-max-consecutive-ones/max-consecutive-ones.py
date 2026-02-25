class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count1 = count2 = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count1 = count1 + 1
            else:
                count2 = max(count1, count2)
                count1 = 0
        return max(count1,count2)