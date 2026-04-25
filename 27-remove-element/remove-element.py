class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
                nums[i] = float('inf')
        i = 0
        while i < len(nums):
            if nums[i] != float('inf'):
                i+=1
            elif nums[i] == float('inf'):
                nums.pop(i)
                nums.append(float('-inf'))
        return len(nums) - count