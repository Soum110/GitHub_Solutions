class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in mapp:
                return [mapp[comp], i]
            mapp[nums[i]] = i
        return []
        