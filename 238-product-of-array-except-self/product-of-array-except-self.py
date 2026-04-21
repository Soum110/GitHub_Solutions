class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        prefix, suffix, res = [1], [1], []
        for i in range(1, len(nums)):
            prefix.append(prefix[-1]* nums[i-1])
        for i in range(len(nums)-2, -1, -1):
            suffix.append(suffix[-1]* nums[i+1])
        suffix = suffix[::-1]

        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        return res